from gym.envs.registration import register

register(
    id='SW1-TEST-v0',
    entry_point='gym_sw1.envs:Sw1TestEnv',
    max_episode_steps=10000
)

register(
    id='SW1-NORMAL-ATTACK-v0',
    entry_point='gym_sw1.envs:NormalAttackEnv',
    max_episode_steps=500
)