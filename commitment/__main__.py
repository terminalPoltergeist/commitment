import sys
import os
import argparse
from .verification import verify
from .directory import directory
from .graphics import app
from .logic import logic

def main():
    # initialize parser and gather arguments
    parser = argparse.ArgumentParser(description='Display git commit history in a graphical interface.', epilog='More: https://github.com/terminalPoltergeist/commitment.git')
    args = parser.parse_args()
    git_repo = verify()
    if git_repo != "":
        directory(git_repo)
        app()
        logic()
    else:
        print("Not a git repository or child.\nOpen a git repository and run 'commitment' again.")

if __name__ == '__main__':
    main()
