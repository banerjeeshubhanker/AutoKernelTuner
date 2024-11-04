
import gym
import numpy as np

class KernelTuningEnv(gym.Env):
    def __init__(self):
        super(KernelTuningEnv, self).__init__()
        self.action_space = gym.spaces.Discrete(3)
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(5,), dtype=np.float32)

    def reset(self):
        return np.zeros(self.observation_space.shape)

    def step(self, action):
        state = np.zeros(self.observation_space.shape)
        reward = 0.0
        done = False
        return state, reward, done, {}
