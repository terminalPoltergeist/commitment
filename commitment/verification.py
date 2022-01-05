import os.path

def verify():
    # current working directory
    path = os.path.abspath(os.getcwd())
    dirs = path.split("/")
    parent = path
    for i in range(len(dirs)):
        if os.path.isdir(path + "/.git/"):
            parent = path 
            break
        path = '/'.join(dirs[:-i])
    return os.path.isdir(parent + "/.git/")
print(verify())

