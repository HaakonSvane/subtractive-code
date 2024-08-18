import shutil

from utils import get_repo, select_commit_selector_strategy, select_subtractive_strategy


def main(repo_path: str, subtractive_strategy: str, commit_selector: str, branch: str):
    try:

        repo = get_repo(repo_path)
        subtractive_strategy = select_subtractive_strategy(subtractive_strategy)
        commit_selector = select_commit_selector_strategy(commit_selector)

        commits = list(repo.iter_commits(branch))
        subtractive_commits = subtractive_strategy.select_subtractive_commits(commits)
        problem_solves = commit_selector.select_commits(subtractive_commits)

        print(f"Found {len(problem_solves)} problem solves")
    finally:
        shutil.rmtree("./.tmp")
