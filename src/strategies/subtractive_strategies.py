from git import Commit, Repo
from abc import abstractmethod
from tqdm import tqdm
from tabulate import tabulate, SEPARATING_LINE


class SubtractiveStrategy:
    @abstractmethod
    def select_subtractive_commits(commits: list[Commit]) -> list[Commit]:
        pass

    @abstractmethod
    def print_stats(
        repo: Repo,
        problem_solved_commits: list[Commit],
        subtractive_commits: list[Commit],
    ) -> None:
        pass


class GitDiffSubtractiveStrategy(SubtractiveStrategy):
    @staticmethod
    def select_subtractive_commits(
        commits,
    ):
        filtered_commits = []
        for commit in tqdm(
            commits,
            desc="Filtering subtractive commits",
            unit=" commits",
            total=float("inf"),
        ):
            diff = commit.stats
            additions = diff.total["insertions"]
            deletions = diff.total["deletions"]
            if additions < deletions:
                filtered_commits.append(commit)
        return filtered_commits

    @staticmethod
    def print_stats(repo, problem_solved_commits, subtractive_commits):
        len_all = len(list(repo.iter_commits()))
        len_problem_solves = len(problem_solved_commits)
        len_sub_commits = len(subtractive_commits)
        strategy_stats = []
        strategy_stats.append(["Repository remote:", repo.remote().url])
        strategy_stats.append(["Total commits:", len_all])
        strategy_stats.append(SEPARATING_LINE)
        strategy_stats.append(["Problem solved commits:", len_problem_solves])
        strategy_stats.append(["Commits with subrtactive fixes:", len_sub_commits])
        strategy_stats.append(
            [
                "Percentage of all problem solves that are subtractive:",
                "{:.2f}%".format(len_sub_commits / len_problem_solves * 100),
            ]
        )

        print(tabulate(strategy_stats))
