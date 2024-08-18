from git import Repo
from tqdm import tqdm
from src.strategies.commit_selector_strategies import *
from src.strategies.subtractive_strategies import *


def get_repo(path: str) -> Repo:
    repo = None
    with tqdm(desc="Fetching git repository", total=float("inf"), unit="items") as pbar:

        def progressCallback(_, cur_count, max_count=None, message=""):
            pbar.update(cur_count)

        repo = Repo.clone_from(path, "./.tmp", progress=progressCallback)
    return repo


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
