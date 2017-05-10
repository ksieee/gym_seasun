import gym
import numpy as np

from gym_sw1.trans.game_socket import GameSocket
from gym_sw1.trans.pb.action_pb2 import Action
from gym_sw1.trans.pb.state_pb2 import State

from bokeh.io import output_notebook, show, push_notebook
from bokeh.plotting import figure
from bokeh.layouts import gridplot

STATE_DIM = 12
ACTION_DIM = 9

WIN_REWARD = 9999
LOSE_REWARD = -9999
DIST_REWARD_WEIGHT = 1
TARGET_HP_REWARD_WEIGHT = 10
ME_HP_REWARD_WEIGHT = 100

MAX_ROUND_COUNT = 500


class NormalAttackEnv(gym.Env):
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

        self.round_count = 0
        self.last_state = None
        self.current_state = None
        self.current_action = None

        self.reward_hist = []

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
        reward = 0;

        if not self.current_state.npc:
            reward = WIN_REWARD

        elif not self.current_state.player.base.hp:
            reward = LOSE_REWARD

        else:
            current_dist_power = np.square(self.current_state.player.base.x - self.current_state.npc.x) \
                                 + np.square(self.current_state.player.base.y - self.current_state.npc.y)
            last_dist_power = np.square(self.last_state.player.base.x - self.last_state.npc.x) \
                              + np.square(self.last_state.player.base.y - self.last_state.npc.y)
            dist_reward = np.sqrt(last_dist_power) - np.sqrt(current_dist_power)
            me_hp_reward = self.current_state.player.base.hp - self.last_state.player.base.hp
            target_hp_reward = self.last_state.npc[0].hp - self.current_state.npc[0].hp
            reward = dist_reward * DIST_REWARD_WEIGHT + me_hp_reward * ME_HP_REWARD_WEIGHT + target_hp_reward * TARGET_HP_REWARD_WEIGHT - self.round_count

        self.reward_hist.append(reward)
        return reward

    def _cal_done(self, state):
        if state.player and (not state.player.hp):
            return True

        if not state.npc:
            return True

        if self.round_count > MAX_ROUND_COUNT:
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

        # init bokeh visualize
        # TODO: 如果可以的话, 把旧图去掉, 并在旧图上更新, 而不是产生新图
        output_notebook()
        min_screen_x, min_screen_y, max_screen_x, max_screen_y, me_x, me_y, target_x, target_y = \
            0, 0, 100, 100, 20, 20, 50, 60
        plt_loc = figure(plot_width=400, plot_height=400, toolbar_location=None,
                         x_range=(min_screen_x, max_screen_x), y_range=(min_screen_y, max_screen_y),
                         title="敌我坐标")
        self.rd_loc = plt_loc.circle([me_x, target_x], [me_y, target_y], size=20, line_color="gold",
                                     fill_color=["green", "firebrick"], fill_alpha=0.6)

        me_hp, me_hp_max, target_hp, target_hp_max = 100, 120, 200, 180
        plt_hp = figure(plot_width=400, plot_height=400, title="hp血量")

        plt_hp.xaxis.visible = False
        plt_hp.xgrid.visible = False

        self.rd_hp = plt_hp.vbar(x=[1, 1, 2, 2], width=0.5, bottom=0,
                     top=[me_hp_max, me_hp, target_hp_max, target_hp], color=["grey", "darkgreen",  "grey", 'red'], alpha=0.6)

        plt_action = figure(plot_width=400, plot_height=400, title="action: 方向+攻击")

        plt_action.xaxis.visible = False
        plt_action.xgrid.visible = False
        plt_action.yaxis.visible = False
        plt_action.ygrid.visible = False
        self.rd_action = plt_action.rect([1, 1, 1, 2, 2, 3, 3, 3, 5], [1, 2, 3, 1, 3, 1, 2, 3, 2], 0.9, 0.9,
                                                   fill_alpha=0.6, color=["silver"]*9, line_color='silver')
        
        # 显示reward趋势
        plt_reward = figure(plot_width=400, plot_height=400, title="reward趋势")
        self.rd_reward = plt_reward.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)

        # put all the plots in a gridplot
        plt_combo = gridplot([[plt_loc, plt_hp], [plt_action, plt_reward]], toolbar_location=None)

        # show the results
        show(plt_combo, notebook_handle=True)

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
            step_action.value = self.current_state.npc[0].id

        state_raw = self.game_socket.send_action(step_action.SerializeToString())
        state = State()
        state.ParseFromString(state_raw)

        self.last_state = self.current_state
        self.current_state = state
        self.current_action = step_action
        self.round_count += 1

        return self._trans_state(state), self._cal_reward(state), self._cal_done(state)

    def _render(self, mode='human', close=False):
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
                action = {'move_up': bool(self.current_action.value.index(0)),
                          'move_up_right': bool(self.current_action.value.index(1)),
                          'move_right': bool(self.current_action.value.index(2)),
                          'move_right_down': bool(self.current_action.value.index(3)),
                          'move_down': bool(self.current_action.value.index(4)),
                          'move_down_left': bool(self.current_action.value.index(5)),
                          'move_left': bool(self.current_action.value.index(6)),
                          'move_left_up': bool(self.current_action.value.index(7)),
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

        self._render_state_action(location, hp, action, self.reward_hist[-50:])

        return

    def _render_state_action(self, location, hp, action, reward):
        # location = {min_screen_x, min_screen_y, max_screen_x, max_screen_y, me_x, me_y, target_x, target_y}
        # hp = {me_hp, me_hp_max, target_hp, target_hp_max}
        # action = {move_up, move_up_right, move_right, move_right_down, move_down, move_down_left, move_left, move_left_up, normal_attack_target}
        # reward = []

        # 更新图表
        self.rd_loc.data_source.data['x'] = [location['me_x'], location['target_x']]
        self.rd_loc.data_source.data['y'] = [location['me_y'], location['target_y']]
        self.rd_hp.data_source.data['top'] = [hp['me_hp'], hp['target_hp'], hp['me_hp_max'], hp['target_hp_max']]
        self.rd_action.data_source.data['fill_color'] = self._transform_action_to_color(action)
        self.rd_reward.data_source.data['y'] = reward
        push_notebook()

        return

    def _transform_action_to_color(action):
        # 按照绘图时格子的序列排列
        all_actions = ['move_down_left',
                       'move_left',
                       'move_left_up',
                       'move_down',
                       'move_up',
                       'move_right_down',
                       'move_right',
                       'move_up_right',
                       'normal_attack_target'
                       ]
        return ['green' if action[_a] else 'silver' for _a in all_actions]
