import os

from git import Repo


def print_repo_details(repo_path='.'):
    try:
        repo = Repo(repo_path)
        if not repo.bare:
            print(f"Repo description: {repo.description}")
            print(f"Active branch: {repo.active_branch.name}")
            commit = repo.head.commit
            print(f"Latest commit hash: {commit.hexsha}")
            print(f"Author: {commit.author.name} <{commit.author.email}>")
            print(f"Date: {commit.authored_datetime}")
            print(f"Message: {commit.message}")
        else:
            print("The repo is bare.")
    except Exception as e:
        print(f'Error accessing repo at "{repo_path}": {e}')


def hello():
    print("hi")


def bye():
    print("bye")


print(hello())

print_repo_details(os.getcwd())
