from gymnasium.envs.registration import register
from copy import deepcopy

from . import datasets

register(
    id="rl_trading/TradingWorld-v0",
    entry_point="rl_trading.envs:TradingWorldEnv",
    kwargs={
        'df': deepcopy(datasets.FOREX_EURUSD_1H_ASK),
    }
)
