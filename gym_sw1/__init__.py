from gym.envs.registration import register
from gym.scoreboard.registration import add_task, add_group
from .package_info import USERNAME

register(
    id='SW1-TEST-V0'.format(USERNAME),
    entry_point='gym.envs.sw1:SW1-TEST-V0',
    max_episode_steps=10000,
)