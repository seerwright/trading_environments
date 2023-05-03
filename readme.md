# Trading Environments
This repository contains Gymnasium-based environments to simulate a market for the purpose of training a reinforcement learning agent.

# How to Use
You must install this environment and then you can use it like any other Gymnasium environment, which is roughly similar to Gym > 0.21.

### Install
* `git clone https://github.com/seerwright/trading_environments.git`
* `pip install -e trading_environments`
* Check installation with `pip list | grep trading_`

<br/>

### Example Use

Create a driver for the agent's training.

``` python
import gymnasium as gym
import rl_trading.envs.trading_world

env = gym.make("rl_trading/TradingWorld-v0", render_mode='human')
observation = env.reset()


while True:
    # Take a random action
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    # Render the game
    env.render()

    if done == True:
        break

env.close()

```

<br/>


If you named the file above `trading_test.py`, for example, then you would simply run it with `python trading_test.py`. 


# License
This is not open source software. You may review the code in this repo, but you may not use it for commercial purposes or (re)distribute it or use it for personal trading. Please refer to the license.txt file in this repo for more information.

PRs may require accompanying PRs in [the documentation repo](https://github.com/Farama-Foundation/Gymnasium/tree/main/docs).
