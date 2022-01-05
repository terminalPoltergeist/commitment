import sys
import os
import argparse
from .verification import verify

def main():
    parser = argparse.ArgumentParser(description='Display git commit history in a graphical interface.', epilog='More: https://github.com/terminalPoltergeist/commitment.git')
    args = parser.parse_args()
    home_dir = os.path.expanduser('~') 
    git_repo = verify()
    if git_repo != "":
        os.system("mkdir " + home_dir + "/.commitment")
        os.system("git log --pretty=format:'%h,%an,%ar,%s' > " + home_dir + "/.commitment/log.csv")


if __name__ == '__main__':
    main()
