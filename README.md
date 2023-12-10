### Step 0: Download and Unzip Carla

Download [Carla version 0.9.14](https://github.com/carla-simulator/carla/releases/tag/0.9.14) from the official source. After downloading, unzip the contents. You do not have to put the contents under the root of this project. To start the simulator, run `CarlaUE4.exe`.

### Step 1: Install the Required Packages

Install the necessary packages by running the following command: `pip install -r requirements.txt`

### Step 2: Train an Agent

Run Script `train_agent.py`
- **Train New Agent**: Use `train_new_model("agent_name", total_timesteps=200000, hyperparams=hyperparams2)` to train a new agent. You can specify the name of the agent, the total number of timesteps for training, and the hyperparameters.

- **Train Existing Agent**: Use `train_exist_model(model_path, total_timesteps=100000, hyperparams=hyperparams2)` to continue training an existing agent. Specify the model path, the total number of timesteps for continued training, and the hyperparameters.

### Step 3: Evaluate an Agent
Run Script `eval_agent.py`
- **Evaluate Agent**: Use `eval_model(model_path)` to evaluate an agent. Specify the path to the model you wish to evaluate.

**Note**:  A pre-trained model was provided. If you want to evaluate this pre-trained agent, please download the model from [this link](https://drive.google.com/drive/folders/1ozd8M5q2DDxoHQIQc6tabHcS8o9_ZQuH) and place the model zip file under path `training/Saved_Models`. In this case, you can directly execute `eval_agent.py` as the default path in the script is the path of this model.

---
## Demo:

We also provided a demo video of the pre-trained agent with 400,000 training timesteps
[Demo Video](https://drive.google.com/file/d/1ijbiKa8CEiVy7xC2KwXqHiyEQwAfEcNM/preview)

---
## About Agent:

Implementation details of our gym environment are in `carla_env/carla_env_multi_obs`

### Observation Spaces: 
[semantic segmentation camera sensor data], [relative position, relative velocity, relative speed]

![Screenshot 2023-12-04 180751](https://github.com/Somdit/MimicPilot/assets/40221390/f9eb0608-4914-4f8d-9fdf-f288b888dbd0)

| Color        | Semantic Segmentation |
|--------------|-----------------------|
| Purple       | Route                 |
| Light Green  | Lane                  |
| Blue         | Vehicle               |
| Black        | Obstacle              |

### Action Spaces:
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
