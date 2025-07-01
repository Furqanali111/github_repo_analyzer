import os

def find_all_files(repo_path):
    """
    Finds all files in the repo.
    Returns a dict with filenames as keys and their full paths as values.
    """
    found = {}
    for root, _, files in os.walk(repo_path):
        for fname in files:
            found[os.path.relpath(os.path.join(root, fname), repo_path)] = os.path.join(root, fname)
    return found