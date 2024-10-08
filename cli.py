import argparse

from main import main

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
        "-p",
        "--problem-selector",
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
        "-v",
        "--verbose-stats",
        help="print statistics of the results to the terminal. Overridden by the `-q` flag",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "-q",
        "--quiet",
        help="suppress all output from the program",
        action="store_true",
        default=False,
    )

    parsed = parser.parse_args()

    main(
        repo_path=parsed.repo_path,
        subtractive_strategy=parsed.subtractive_strategy,
        problem_solve_selector=parsed.problem_selector,
        branch=parsed.branch,
        quiet=parsed.quiet,
        print_stats=parsed.verbose_stats,
    )
