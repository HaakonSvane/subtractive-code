import shutil

from src.utils import (
    get_repo,
    select_commit_selector_strategy,
    select_subtractive_strategy,
)
from src.analysis_results import AnalysisResults


def main(
    repo_path: str,
    subtractive_strategy: str,
    commit_selector: str,
    branch: str,
    print_stats: bool = False,
) -> AnalysisResults:
    try:

        repo = get_repo(repo_path)
        selected_subtractive_strategy = select_subtractive_strategy(
            subtractive_strategy
        )
        selected_commit_selector = select_commit_selector_strategy(commit_selector)

        commits = list(repo.iter_commits(branch))
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
