
import gym
from stable_baselines3 import PPO
from rl_tuner.environment import KernelTuningEnv

def train_model():
    env = KernelTuningEnv()
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=10000)
    model.save("kernel_tuner_model")

if __name__ == "__main__":
    train_model()
