import gym

import matplotlib.pyplot as plt
import numpy as np

class NormalAttackEnv(gym.Env):
    def __init__(self):
        # me_x, me_y, me_hp, me_hp_max, me_face_to, me_speed, target_x, target_y, target_hp, target_hp_max, target_face_to, target_speed
        self.observation_space = gym.spaces.Box(float("-inf"), float("inf"), (12,))
        # {0,1,2,3,4,5,6,7,8} = {move_up, move_up_right, move_right, move_right_down, move_down, move_down_left, move_left, move_left_up, normal_attack_target}
        self.action_space = gym.spaces.Discrete(9)

    def _reset(self):
        return

    def _close(self):
        return

    def _step(self, action):
        return
