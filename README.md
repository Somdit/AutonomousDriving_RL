### Step 0: Download and Unzip Carla

Download [Carla version 0.9.14](https://github.com/carla-simulator/carla/releases/tag/0.9.14) from the official source. After downloading, unzip the contents. You do not have to put the contents under the root of this project. To start the simulator, run `CarlaUE4.exe`.

### Step 1: Install the Required Packages

Install the necessary packages by running the following command: `pip install -r requirements.txt`

### Step 2:Train an Agent

Run Script `train_agent.py`
- Train New Model: `train_new_model("PPO_highway_lane_tracking", total_timesteps=200000, hyperparams=hyperparams2)`
- Train Exist Model: `train_exist_model(model_path, total_timesteps=100000, hyperparams=hyperparams2)`
- Evaluate Model: `train_exist_model(model_path, total_timesteps=100000, hyperparams=hyperparams2)`

---
## About Agent:

#### Observation Spaces: 
[semantic segmentation camera sensor data], [relative position, relative velocity, relative speed]

![Screenshot 2023-12-04 180751](https://github.com/Somdit/MimicPilot/assets/40221390/f9eb0608-4914-4f8d-9fdf-f288b888dbd0)

| Color        | Semantic Segmentation |
|--------------|-----------------------|
| Purple       | Route                 |
| Light Green  | Lane                  |
| Blue         | Vehicle               |
| Black        | Obstacle              |

#### Action Spaces:
| Action   | Space       | Range    |
|----------|-------------|----------|
| Throttle | Continuous  | [-1, 1]  |
| Steer    | Continuous  | [-1, 1]  |
| Brake    | Continuous  | [0, 1]   |

---
## Current Plans:
| Plan                        | Description                            | Status |
|-----------------------------|----------------------------------------|--------|
| Learning to be Malicious | Train the agent to imitate human-driven malicious attacks for automated benchmark testing | ⏳     |
