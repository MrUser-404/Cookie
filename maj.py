from git import Repo

repo_path = 'Test.py'
repo = Repo(repo_path)
repo.git.pull()
