from gym import Env

import matplotlib.pyplot as plt
import numpy as np

class Sw1TestEnv(Env):
    def __init__(self):
        # print('init sw1 test env')
        self.observation_space = np.array([1])
        self.action_space = np.array([1])

    def _get_x_y(self):
        x = np.linspace(-1, 1, 500)
        y = 2 * x + 1
        return x, y

    def _reset(self):
        # print('reset sw1 test env')
        x, y = self._get_x_y()
        plt.ion()
        plt.close('all')
        plt.figure(num='Test Figure')
        plt.plot(x, y)
        plt.draw()
        plt.pause(0.1)

        self.step_count = 0
        self.current_state = np.random.uniform(low=-1,high=1,size=[1])
        return self.current_state

    def _close(self):
        # print('close sw1 test env')
        plt.close('all')

    def _step(self, action):
        # print('step sw1 test env')
        curr_x = self.current_state[0]
        curr_y = 2 * curr_x + 1
        y = action[0]

        plt.plot(curr_x, y, 'rx')
        plt.draw()
        plt.pause(0.1)

        self.step_count += 1
        self.current_state = np.random.uniform(low=-1,high=1,size=[1])

        return self.current_state, -np.abs(y - curr_y), self.step_count >=5, None
