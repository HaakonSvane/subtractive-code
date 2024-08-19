from abc import abstractmethod

from git import Commit
from tqdm import tqdm

from src.strategies.utils.repo import is_quiet_mode


class CommitSelectorStratgy:
    @abstractmethod
    def select_commits(commits: list[Commit]) -> list[Commit]:
        pass


class SemanticCommitSelectorStrategy(CommitSelectorStratgy):
    @staticmethod
    def select_commits(commits):
        filtered_commits = []
        for commit in tqdm(
            commits,
            desc="Finding 'fix' commits",
            unit=" commits",
            total=float("inf"),
            disable=is_quiet_mode(),
        ):
            if "fix" in commit.message:
                filtered_commits.append(commit)

        return filtered_commits
