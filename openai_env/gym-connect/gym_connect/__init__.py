from gym.envs.registration import register

register(
    id="connect-v0",
    entry_point="gym_connect.envs:ConnectEnv",
)
register(
    id="connect-extrahard-v0",
    entry_point="gym_connect.envs:ConnectExtraHardEnv",
)
