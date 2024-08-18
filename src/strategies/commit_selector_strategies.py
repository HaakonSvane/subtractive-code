from abc import abstractmethod
from git import Commit
from tqdm import tqdm


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
        ):
            if "fix" in commit.message:
                filtered_commits.append(commit)

        return filtered_commits
