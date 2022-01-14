import os

parent = ""
def verify():
    # current working directory
    path = os.path.abspath(os.getcwd())
    dirs = path.split("/")
    for i in range(len(dirs)):
        if os.path.isdir(path + "/.git/"):
            parent = path 
            break
        path = '/'.join(dirs[:-i])
    return parent

