"""
Functions to do with parsing the algorithm summaries
"""

from pathlib import Path


def fetch_alg_descriptions() -> dict:
    """
    Fetch the name and summary of each algorithm
    """
    algs: dict[str, str] = {}
    for filepath in Path("src/algo_chooser/algorithm_summaries").glob("*.md"):
        with open(filepath, "r") as file:
            algs[filepath.stem] = file.read()

    return algs
