from gym import Env

import matplotlib.pyplot as plt
import numpy as np

class Sw1TestEnv(Env):
    def __init__(self):
        # print('init sw1 test env')
        self.observation_space = np.array([1])
        self.action_space = np.array([1])

    def _get_y(self, x):
        return x ** 2 + 0.5 * x + 1

    def _reset(self):
        # print('reset sw1 test env')
        x = np.linspace(-1, 1, 500)
        y = self._get_y(x)
        plt.ion()
        plt.close('all')
        plt.figure(num='Test Figure')
        plt.plot(x, y)
        plt.draw()
        plt.pause(0.0001)

        self.step_count = 0
        self.current_state = np.random.uniform(low=-1,high=1,size=[1])
        return self.current_state

    def _close(self):
        # print('close sw1 test env')
        plt.close('all')

    def _step(self, action):
        # print('step sw1 test env')
        curr_x = self.current_state[0]
        curr_y = self._get_y(curr_x)
        y = action[0]

        plt.plot(curr_x, y, 'rx')
        plt.draw()
        plt.pause(0.0001)

        self.step_count += 1
        self.current_state = np.random.uniform(low=-1,high=1,size=[1])

        return self.current_state, -np.abs(y - curr_y) * 10, self.step_count >=5, None
