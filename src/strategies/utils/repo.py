from git import Repo
from tqdm import tqdm

from src.strategies.utils.is_quiet_mode import is_quiet_mode


def get_repo(path: str) -> Repo:
    repo = None
    with tqdm(
        desc="Fetching git repository",
        total=float("inf"),
        unit="items",
        disable=is_quiet_mode(),
    ) as pbar:

        def progressCallback(_, cur_count, max_count=None, message=""):
            pbar.update(cur_count)

        repo = Repo.clone_from(path, "./.tmp", progress=progressCallback)
    return repo
