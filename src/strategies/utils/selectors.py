from src.strategies.subtractive_strategies import (
    GitDiffSubtractiveStrategy,
    SubtractiveStrategy,
)
from src.strategies.commit_selector_strategies import (
    CommitSelectorStratgy,
    SemanticCommitSelectorStrategy,
)


def select_subtractive_strategy(strategy: str) -> SubtractiveStrategy:
    strategy_map: dict[str, SubtractiveStrategy] = {"diff": GitDiffSubtractiveStrategy}
    if not strategy_map.get(strategy):
        raise ValueError(f"Unknown strategy: {strategy}")
    return strategy_map.get(strategy)


def select_commit_selector_strategy(strategy: str) -> CommitSelectorStratgy:
    strategy_map: dict[str, CommitSelectorStratgy] = {
        "semantic": SemanticCommitSelectorStrategy
    }
    if not strategy_map.get(strategy):
        raise ValueError(f"Unknown strategy: {strategy}")
    return strategy_map.get(strategy)
