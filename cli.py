import argparse
from main import main
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="subtractive-analyzer",
        description="Small tool to analyze git repositories for subtractive problem solving",
    )
    parser.add_argument(
        "repo_path",
        help="path to the git repository (can be either a folder or a GitHub Url)",
    )

    parser.add_argument(
        "-s",
        "--subtractive-strategy",
        help="strategy to use for determining if a commit is a subtractive fix",
        default="diff",
        choices=["diff"],
    )

    parser.add_argument(
        "-c",
        "--commit-selector",
        help="strategy to use for determining if a commit should be counted as a fix (a 'problem solve')",
        default="semantic",
        choices=["semantic"],
    )

    parser.add_argument(
        "-b",
        "--branch",
        help="git branch to work from",
        default="main",
    )

    parser.add_argument(
        "-p",
        "--print-stats",
        help="print statistics of the results to the terminal",
        action="store_true",
        default=False,
    )

    parsed = parser.parse_args()

    main(
        parsed.repo_path,
        parsed.subtractive_strategy,
        parsed.commit_selector,
        parsed.branch,
        parsed.print_stats,
    )
