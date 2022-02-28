import sys
import os
import argparse
import subprocess
import tkinter as tk
from tkinter.ttk import *

class Backend:
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
            self.http_url = ('https://github.com/' + self.username + '/' + self.project_name) #add '/tree/*commit hash*' to get full repo at commit, replace '/tree/' with '/commit/' to go to specific commit
            # get git tree info and save to ~/.commitment/log.csv
            self.pull_data()
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

class Graphics(tk.Tk):
    def __init__(self, backend):
        super().__init__()
        self.geometry("500x750")
        self.center(self)
        project = backend.project_name
        self.title("Commitment - " + project)
        self.canvas = tk.Canvas(self)
        self.canvas.create_oval(10,10,80,80, outline="#f11", fill="#1f1", width=2)
        self.canvas.pack()
        self.mainloop()
    # solution from https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter
    def center(self,win):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()





def main():
    # initialize parser and gather arguments
    parser = argparse.ArgumentParser(description='Display git commit history in a graphical interface.', epilog='More: https://github.com/terminalPoltergeist/commitment.git')
    args = parser.parse_args()
    inst = Backend()
    graph = Graphics(inst)

if __name__ == '__main__':
    main()
