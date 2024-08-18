from abc import abstractmethod
from git import Commit
from tqdm import tqdm
from typing import Generator, Union


class CommitSelectorStratgy:
    @abstractmethod
    def select_commits(
        commits: Union[Generator[Commit, None, None], list[Commit]]
    ) -> Union[Generator[Commit, None, None], list[Commit]]:
        pass


class SemanticCommitSelectorStrategy(CommitSelectorStratgy):
    @staticmethod
    def select_commits(commits):
        for commit in tqdm(
            commits,
            desc="Finding subtractive commits",
            unit="commits",
            total=float("inf"),
        ):
            if "fix" in commit.message:
                yield commit
