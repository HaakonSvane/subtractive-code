import os


def is_quiet_mode() -> bool:
    return os.environ.get("QUIET", "False") == "True"
