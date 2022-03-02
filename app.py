import github
from github import GithubException
import requests

g = github.Github("9d76f2557ac81e158469e5fae9256e48b548e894")

# or if you are using login and password g = github.Github(login, password)
repo = g.get_repo("smartinternz02/SI-GuidedProject-6670-1638183039")

try:
    # get repo content from root directory
    repo.get_contents("/")
    print(repo.get_contents("/"))
except GithubException as e:
    print(e.args[1]['message'])
    # output: This repository is empty.
