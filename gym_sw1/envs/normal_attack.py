import gym
import gym.spaces
import numpy as np

from gym_sw1.plot.dashboard import NormalAttackDashboard
from gym_sw1.trans.game_socket import GameSocket
from gym_sw1.trans.pb.action_pb2 import Action
from gym_sw1.trans.pb.state_pb2 import State

STATE_DIM = 12
ACTION_DIM = 9

WIN_REWARD = 300
LOSE_REWARD = -300
DIST_REWARD_WEIGHT = 1
TARGET_HP_REWARD_WEIGHT = 10
ME_HP_REWARD_WEIGHT = 10
ROUND_REWARD_WEIGHT = 10
MAX_DIST = 900
MAX_ROUND_COUNT = 50


class NormalAttackEnv(gym.Env):
    metadata = {'render.modes': ['human', 'rgb_array']}

    def init_params(self, game_ip, game_port):
        self.game_socket = GameSocket(game_ip, game_port)

    def __init__(self):
        self.game_socket = None

        # me_x, me_y, me_hp, me_hp_max, me_face_to, me_speed,
        # target_x, target_y, target_hp, target_hp_max, target_face_to, target_speed
        self.observation_space = gym.spaces.Box(float("-inf"), float("inf"), (STATE_DIM,))

        # {0,1,2,3,4,5,6,7,8} =
        # {move_up, move_up_right, move_right, move_right_down, move_down,
        # move_down_left, move_left, move_left_up, normal_attack_target}
        self.action_space = gym.spaces.Discrete(ACTION_DIM)

        self.episode_count = 0
        self.round_count = 0
        self.last_state = None
        self.current_state = None
        self.current_action = None

        self.reward_hist = []

        self.learning_dashboard = NormalAttackDashboard()

    @classmethod
    def _trans_state(cls, state):
        result = list()

        if state.player:
            result.append(state.player.base.x)
            result.append(state.player.base.y)
            result.append(state.player.base.hp)
            result.append(state.player.base.hp_m)
            result.append(state.player.base.face_to)
            result.append(state.player.base.move_speed)
        else:
            result.extend([0, 0, 0, 0, 0, 0])

        if state.npc:
            result.append(state.npc[0].x)
            result.append(state.npc[0].y)
            result.append(state.npc[0].hp)
            result.append(state.npc[0].hp_m)
            result.append(state.npc[0].face_to)
            result.append(state.npc[0].move_speed)
        else:
            result.extend([0, 0, 0, 0, 0, 0])

        return result

    def _cal_reward(self):
        reward = 0

        if not self.current_state.npc:
            reward = WIN_REWARD
        elif not self.current_state.player.base.hp:
            reward = LOSE_REWARD
        elif self._cal_dist() > MAX_DIST:
            reward = LOSE_REWARD
        else:
            current_dist_power = np.square(self.current_state.player.base.x - self.current_state.npc[0].x) \
                                 + np.square(self.current_state.player.base.y - self.current_state.npc[0].y)

            last_dist_power = np.square(self.last_state.player.base.x - self.last_state.npc[0].x) \
                              + np.square(self.last_state.player.base.y - self.last_state.npc[0].y)
            dist_reward = np.sqrt(last_dist_power) - np.sqrt(current_dist_power)
            me_hp_reward = self.current_state.player.base.hp - self.last_state.player.base.hp
            target_hp_reward = self.last_state.npc[0].hp - self.current_state.npc[0].hp

            reward = dist_reward * DIST_REWARD_WEIGHT + me_hp_reward * ME_HP_REWARD_WEIGHT + target_hp_reward * TARGET_HP_REWARD_WEIGHT - self.round_count * ROUND_REWARD_WEIGHT

        self.reward_hist.append(reward)
        return reward

    def _cal_dist(self):
        current_dist_power = np.square(self.current_state.player.base.x - self.current_state.npc[0].x) \
                             + np.square(self.current_state.player.base.y - self.current_state.npc[0].y)
        return np.sqrt(current_dist_power)

    def _cal_done(self, state):
        if state.player and state.player.base and (not state.player.base.hp):
            return True

        if not state.npc:
            return True

        if self.round_count > MAX_ROUND_COUNT or self._cal_dist() > MAX_DIST:
            return True

        return False

    def _reset(self):
        reset_action = Action()
        reset_action.type = Action.RESET

        state_raw = self.game_socket.send_action(reset_action.SerializeToString())
        state = State()
        state.ParseFromString(state_raw)

        self.current_state = state
        self.round_count = 0
        self.episode_count += 1
        self.reward_hist = []

        return self._trans_state(state)

    def _close(self):
        self.game_socket.close()
        return

    def _step(self, action):
        step_action = Action()
        int_action = int(action)
        if int_action < 8:
            step_action.type = Action.MOVE
            step_action.value.extend([int_action])
        else:
            step_action.type = Action.SKILL_TO_TARGET
            step_action.value.extend([self.current_state.player.skills[0].id, self.current_state.npc[0].id])

        state_raw = self.game_socket.send_action(step_action.SerializeToString())
        state = State()
        state.ParseFromString(state_raw)

        self.last_state = self.current_state
        self.current_state = state
        self.current_action = step_action
        self.round_count += 1

        return self._trans_state(state), self._cal_reward(), self._cal_done(state), None

    def _render(self, mode='human', close=False):
        if (not self.current_action) or (not self.current_state):
            return

        if self.current_state.screen and self.current_state.player and self.current_state.npc:
            location = {'min_screen_x': self.current_state.screen.min_screen_x,
                        'min_screen_y': self.current_state.screen.min_screen_y,
                        'max_screen_x': self.current_state.screen.max_screen_x,
                        'max_screen_y': self.current_state.screen.max_screen_y,
                        'me_x': self.current_state.player.base.x,
                        'me_y': self.current_state.player.base.y,
                        'target_x': self.current_state.npc[0].x,
                        'target_y': self.current_state.npc[0].y}

            hp = {'me_hp': self.current_state.player.base.hp,
                  'me_hp_max': self.current_state.player.base.hp_m,
                  'target_hp': self.current_state.npc[0].hp,
                  'target_hp_max': self.current_state.npc[0].hp_m}

            if self.current_action.type == Action.MOVE:
                action = {'move_up': bool(self.current_action.value[0] == 0),
                          'move_up_right': bool(self.current_action.value[0] == 1),
                          'move_right': bool(self.current_action.value[0] == 2),
                          'move_right_down': bool(self.current_action.value[0] == 3),
                          'move_down': bool(self.current_action.value[0] == 4),
                          'move_down_left': bool(self.current_action.value[0] == 5),
                          'move_left': bool(self.current_action.value[0] == 6),
                          'move_left_up': bool(self.current_action.value[0] == 7),
                          'normal_attack_target': False}
            if self.current_action.type == Action.SKILL_TO_TARGET:
                action = {'move_up': False,
                          'move_up_right': False,
                          'move_right': False,
                          'move_right_down': False,
                          'move_down': False,
                          'move_down_left': False,
                          'move_left': False,
                          'move_left_up': False,
                          'normal_attack_target': True}
            self._render_state_action(location, hp, action, self.reward_hist, self.episode_count)

        return

    def _render_state_action(self, location, hp, action, reward, episode_count):
        # location = {min_screen_x, min_screen_y, max_screen_x, max_screen_y, me_x, me_y, target_x, target_y}
        # hp = {me_hp, me_hp_max, target_hp, target_hp_max}
        # action = {move_up, move_up_right, move_right, move_right_down, move_down, move_down_left, move_left, move_left_up, normal_attack_target}
        # reward = []
        env_data = [location, hp, action, reward, episode_count]
        self.learning_dashboard.update_plots(env_data)
        return
