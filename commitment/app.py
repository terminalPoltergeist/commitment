import os.path

# current working directory
path = os.path.abspath(os.getcwd())
dirs = path.split("/")
for i in range(len(dirs)):
    # print(str(i) + path)
    print(path, os.path.isdir(path + "/.git/"))
    path = '/'.join(dirs[:-i])
# print(os.path.isdir(path + "/.git/"))
