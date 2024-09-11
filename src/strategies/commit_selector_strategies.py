from abc import abstractmethod

from git import Commit
from tqdm import tqdm
import re

from src.strategies.utils.repo import is_quiet_mode


class CommitSelectorStrategy:
    @abstractmethod
    def select_commits(commits: list[Commit]) -> list[Commit]:
        pass


class SemanticCommitSelectorStrategy(CommitSelectorStrategy):
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
            if re.search(
                r"^(fix){1}(\([\w\-\.]+\))?(!)?: ([\w ])+([\s\S]*)",
                commit.message,
                re.IGNORECASE,
            ):
                filtered_commits.append(commit)

        return filtered_commits
