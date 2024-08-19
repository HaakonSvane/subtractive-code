import os
import shutil

from src.analysis_results import AnalysisResults
from src.strategies.utils.repo import get_repo
from src.strategies.utils.selectors import (
    select_commit_selector_strategy,
    select_subtractive_strategy,
)


def main(
    repo_path: str,
    subtractive_strategy: str,
    problem_solve_selector: str,
    branch: str,
    quiet: bool = False,
    print_stats: bool = False,
) -> AnalysisResults:
    try:
        os.environ["QUIET"] = str(quiet)
        repo = get_repo(repo_path)
        repo.git.checkout(branch)
        selected_subtractive_strategy = select_subtractive_strategy(
            subtractive_strategy
        )
        selected_commit_selector = select_commit_selector_strategy(
            problem_solve_selector
        )

        commits = list(repo.iter_commits())
        selected_commits = selected_commit_selector.select_commits(commits)
        subtractive_commits = selected_subtractive_strategy.select_subtractive_commits(
            selected_commits
        )
        if print_stats:
            selected_subtractive_strategy.print_stats(
                repo, selected_commits, subtractive_commits
            )

        return AnalysisResults(
            problem_solved_commits=len(selected_commits),
            subtractive_commits=len(subtractive_commits),
        )

    finally:
        shutil.rmtree("./.tmp")
