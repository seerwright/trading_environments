from gymnasium.envs.registration import register

register(
    id="rl_trading/TradingWorld-v0",
    entry_point="rl_trading.envs:TradingWorldEnv",
)
