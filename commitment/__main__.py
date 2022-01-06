import sys
import os
import argparse
from .verification import verify
from .directory import directory

def main():
    # initializes parser and gathers arguments
    parser = argparse.ArgumentParser(description='Display git commit history in a graphical interface.', epilog='More: https://github.com/terminalPoltergeist/commitment.git')
    args = parser.parse_args()
    git_repo = verify()
    if git_repo != "":
        directory(git_repo)

if __name__ == '__main__':
    main()
