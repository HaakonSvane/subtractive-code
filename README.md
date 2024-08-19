# Subtractive code
A small Python cli for analyzing git repositories for subtractive code

## What is subtractive code?
Subtractive code is a term used to describe code changes that solve a specific problem using subtractive transformations.
Subtractive problem solving is defined by [Adams et al., 2021](https://www.nature.com/articles/s41586-021-03380-y) as:
> We conceptualize subtraction and addition as action categories that remove components from or add components to the original, respectively. When a transformed state has fewer components than the original (for example, a revision with fewer words or a process with fewer obstacles), we describe it as a subtractive transformation; when a transformed state has more components than the original, we describe it as an additive transformation.


## Setup
Set up a virual environment and install all requirements with `pip install -r requirements.txt`

## How does the python CLI work?
You can run the script in CLI mode using `python cli.py`. Use option `-h` for help on the parameters. Below is a table of all cli args:

| arg | description | required | default value |
|---|---|---|---|
|`repo_path` (positional arg) | path to the git repository (can be either a local folder or a git-clonable url) | YES | |
| `-h`, `--help` | Show a help message and exit the program | NO | |
| `-s`, `--subtractive-strategy` | strategy to use for determining if a commit is a subtractive fix | NO | `diff` |
| `-p`, `--problem-selector` | strategy to use for determining if a commit should be counted as a fix (a 'problem solve') | NO | `semantic` |
| `-b`, `--branch` | git branch to work from | NO | `main` |
| `-v`, `--verbose-stats` | print statistics of the results to the terminal. Overridden by the `-q` flag | NO | `False` |
| `-q`, `--quiet` | suppress all output from the program | NO | `False` |

## Strategies
The code for the tool is set up to support multiple strategies for resolving two key components needed for analysis. You are free to contribute with more strategies if you feel that they are either too simple, or lacking. 
These two components are:
1. What code change consitutue a 'problem solve'?
2. What should our rule for determining whether or not a code change is to be considered subtractive or additive?


### 1. Commit selector strategies
Code grows and shrinks over time. It is not uncommon for a software system to grow in terms of features. With new functionality often comes _more_ code. In order to filter out code that is written to support new features, the default strategy for selecting commits to analyze is to only include commits that are semantically tagged with a `fix` commit message. This strategy is named `semantic`.

### 2. Sutractive strategies
There are tons of ways to measure code-complexity. I have included a very simple one that is based on a simple but effective metric, which is the number of lines of code in our application. Each commit provides insights into the diff, which is the number of new lines added minus the number lines removed. If this total is negative, the commit is deemed subtractive. This strategy is named `diff`.