import carla
import os
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from carla_env.carla_env_multi_obs import CarlaEnv
from utils.clean_actors import clean_actors

def eval_model(model_path):
    # evaluate the model
    env = lambda: CarlaEnv()
    env = DummyVecEnv([env])

    model = PPO.load(model_path, env=env, verbose=1)

    obs = env.reset()
    while True:
        action, _states = model.predict(obs, deterministic=True)
        obs, rewards, dones, info = env.step(action)
        env.render(mode='human')

if __name__ == '__main__':
    # connect to simulator
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)

    # initialize world
    world = client.get_world()
    client.load_world('Town05')

    # init carla environment
    clean_actors()

    model_path = os.path.join('./Training/Saved_Models/PPO_highway_lane_tracking')  # .zip at the end of file not require
    eval_model(model_path)
