from git import Commit
from abc import abstractmethod
from tqdm import tqdm
from typing import Generator, Union


class SubtractiveStrategy:
    @abstractmethod
    def select_subtractive_commits(
        commits: Union[Generator[Commit, None, None], list[Commit]]
    ) -> Union[Generator[Commit, None, None], list[Commit]]:
        pass


class GitDiffSelectorStrategy(SubtractiveStrategy):
    @staticmethod
    def select_subtractive_commits(
        commits,
    ):
        for commit in tqdm(
            commits,
            desc="Filtering subtractive commits",
            unit="commits",
            total=float("inf"),
        ):
            diff = commit.stats
            additions = diff.total["insertions"]
            deletions = diff.total["deletions"]
            if additions < deletions:
                yield commit
