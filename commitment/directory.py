import os

def directory(path):
    home_dir = os.path.expanduser('~') 
    if not os.path.isdir(home_dir + "/.commitment"):
        os.system("mkdir " + home_dir + "/.commitment")
    os.system("git log --pretty=format:'%h,%an,%ar,%s, %D' --all > " + home_dir + "/.commitment/log.csv")
    

