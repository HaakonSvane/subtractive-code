from dataclasses import dataclass


@dataclass
class AnalysisResults:
    problem_solved_commits: int
    subtractive_commits: int
