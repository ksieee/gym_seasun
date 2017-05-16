# -*- coding: utf-8 -*-
from bokeh.io import output_notebook, show, push_notebook
from bokeh.plotting import figure
from bokeh.layouts import gridplot
import numpy as np

# ! only used to temporarily shutdown bokeh warning !
import warnings
warnings.filterwarnings('ignore')
# TODO: solve warning below
# \site-packages\bokeh\models\sources.py:89: BokehUserWarning: ColumnDataSource's columns must be of the same length
#  lambda: warnings.warn("ColumnDataSource's columns must be of the same length", BokehUserWarning))


class NormalAttackDashboard:
    """A dashboard to visualize RL learning performance on normal attack"""

    def __init__(self):
        output_notebook()
        min_screen_x, min_screen_y, max_screen_x, max_screen_y, me_x, me_y, target_x, target_y = \
            0, 0, 100, 100, 20, 20, 50, 60
        plt_loc = figure(plot_width=400, plot_height=400, toolbar_location=None,
                         x_range=(min_screen_x, max_screen_x), y_range=(max_screen_y, min_screen_y),
                         x_axis_location="above", title="敌我距离")  # use up-left corner as origin
        plt_loc.title.align = "center"
        plt_loc.title.text_color = "orange"
        plt_loc.title.text_font_size = "25px"
        plt_loc.title.background_fill_color = "blue"

        self.plt_loc = plt_loc  # 用于后续更新边界和标题中的距离显示
        self.rd_loc = plt_loc.circle([me_x, target_x], [me_y, target_y], size=20, line_color="gold",
                                     fill_color=["green", "firebrick"], fill_alpha=0.6)

        me_hp, me_hp_max, target_hp, target_hp_max = 100, 120, 180, 200
        plt_hp = figure(plot_width=400, plot_height=400, title="hp血量")

        plt_hp.xaxis.visible = False
        plt_hp.xgrid.visible = False

        self.rd_hp = plt_hp.vbar(x=[1, 1, 2, 2], width=0.5, bottom=0,
                                 top=[me_hp_max, me_hp, target_hp_max, target_hp],
                                 color=["grey", "darkgreen", "grey", 'red'], alpha=0.6)

        plt_action = figure(plot_width=400, plot_height=400, title="action: 方向+攻击")

        plt_action.xaxis.visible = False
        plt_action.xgrid.visible = False
        plt_action.yaxis.visible = False
        plt_action.ygrid.visible = False
        self.rd_action = plt_action.rect([1, 1, 1, 2, 2, 3, 3, 3, 5], [1, 2, 3, 1, 3, 1, 2, 3, 2],
                                         0.9, 0.9, fill_alpha=0.6,
                                         color=["silver"] * 9, line_color='silver')

        # 显示reward趋势
        plt_reward = figure(plot_width=400, plot_height=400, title="last reward: ")
        plt_reward.title.align = "center"
        plt_reward.title.text_color = "green"
        plt_reward.title.text_font_size = "20px"
        plt_reward.title.background_fill_color = "black"
        self.plt_reward = plt_reward  # 用于后续更新标题中的reward值
        self.rd_reward = plt_reward.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)

        # put all the plots in a gridplot
        plt_combo = gridplot([[plt_loc, plt_hp], [plt_action, plt_reward]], toolbar_location=None)

        # show the results
        show(plt_combo, notebook_handle=True)

    def update_plots(self, env_state_action):
        """update bokeh plots according to new env state and action data"""
        location, hp, action, reward, episode_count = env_state_action

        # calc Euclidean Distance
        _coords1 = np.array([location['me_x'], location['me_y']])
        _coords2 = np.array([location['target_x'], location['target_y']])
        eucl_dist = np.sqrt(np.sum((_coords1 - _coords2) ** 2))  # alternative way: np.linalg.norm(_coords1 - _coords2)
        self.plt_loc.title.text = "敌我距离: {:12.2f}".format(eucl_dist)
        self.plt_loc.x_range.start = location["min_screen_x"]
        self.plt_loc.x_range.end = location["max_screen_x"]
        self.plt_loc.y_range.start = location["max_screen_y"]
        self.plt_loc.y_range.end = location["min_screen_y"]
        self.rd_loc.data_source.data['x'] = [location['me_x'], location['target_x']]
        self.rd_loc.data_source.data['y'] = [location['me_y'], location['target_y']]
        self.rd_hp.data_source.data['top'] = [hp['me_hp_max'], hp['me_hp'],
                                              hp['target_hp_max'], hp['target_hp'], ]
        self.rd_action.data_source.data['fill_color'] = self._transform_action_to_color(action)
        self.rd_reward.data_source.data['x'] = range(len(reward))
        self.rd_reward.data_source.data['y'] = reward
        self.plt_reward.title.text = "#{} episode -- reward: {:5}".format(episode_count, reward[-1] if reward else "")
        push_notebook()

    def _transform_action_to_color(self, action):
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
