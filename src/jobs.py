from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        file_jobs = csv.DictReader(file)
        list_jobs = list(file_jobs)
    return list_jobs

    """Reads a file from a given path and returns its contents
    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    # return []
