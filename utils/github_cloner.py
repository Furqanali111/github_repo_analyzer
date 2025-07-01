import os
from git import Repo, GitCommandError

def clone_github_repo(repo_url: str, dest_folder: str = "temp_repos") -> str:
    """
    Clones the given GitHub repository URL into the temp_repos folder.
    Returns the path to the cloned repository.
    """
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    repo_name = repo_url.rstrip('/').split('/')[-1].replace('.git', '')
    repo_path = os.path.join(dest_folder, repo_name)
    try:
        Repo.clone_from(repo_url, repo_path)
    except GitCommandError as e:
        raise RuntimeError(f"Failed to clone repo: {e}")
    return repo_path