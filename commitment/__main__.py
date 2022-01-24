import sys
import os
import argparse
import subprocess
#from .graphics import app

class Instance:
    def __init__(self):
        # directory where application is run
        self.dir = os.path.abspath(os.getcwd())
        # root directory of git repository
        self.root = self.get_repo()
        # home directory of user
        self.home = os.path.expanduser('~')
        if self.root != "":
            # list of branches of git repository
            self.branches = os.listdir(self.root + "/.git/refs/heads")
            # url (ssh or http) of remote repository
            self.remote_url = subprocess.check_output(['git', 'remote', 'get-url', 'origin'])
            # name of repository
            self.project_name = subprocess.check_output(['basename', self.remote_url, '.git']).decode('ascii').replace('.git', '').strip()
            # username of git user
            self.username = subprocess.check_output(['git', 'config', 'user.name']).decode('ascii').strip()
            # http url of remote repository
            self.http_url = 'https://github.com/' + self.username + '/' + self.project_name) #add '/tree/*commit hash*' to get full repo at commit, replace '/tree/' with '/commit/' to go to specific commit
        else:
            print("Not a git repository or child of git repository. Change to a git repository and run again")
    def get_repo(self):
        parent = ""
        path = self.dir
        # current working directory
        dirs = path.split("/")
        for i in range(len(dirs)):
            if os.path.isdir(path + "/.git/"):
                parent = path 
                break
            path = '/'.join(dirs[:-i])
        return parent
    def pull_data(self):
        if not os.path.isdir(self.home + "/.commitment"):
            os.system("mkdir " + self.home + "/.commitment")
        os.system("git log --pretty=format:'%h,%an,%ar,%s, %D' --all > " + self.home + "/.commitment/log.csv")




def main():
    # initialize parser and gather arguments
    parser = argparse.ArgumentParser(description='Display git commit history in a graphical interface.', epilog='More: https://github.com/terminalPoltergeist/commitment.git')
    args = parser.parse_args()
    inst = Instance()

if __name__ == '__main__':
    main()
