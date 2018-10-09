from gym.envs.registration import register

register(
    id='gym-torcs-v0',
    entry_point='madras.envs:TorcsEnv',
)

register(
    id='gym-madras-v0',
    entry_point='madras.envs:MadrasEnv',
)
