import os
import subprocess
from .verification import verify

def logic():
    branches = os.listdir(verify() + "/.git/refs/heads")
    remote = subprocess.check_output(['git', 'remote', 'get-url', 'origin'])
    project = subprocess.check_output(['basename', remote, '.git']).decode('ascii').replace('.git', '').strip()
    name = subprocess.check_output(['git', 'config', 'user.name']).decode('ascii').strip()
    print('https://github.com/' + name + '/' + project) #add '/tree/*commit hash*' to get full repo at commit, replace '/tree/' with '/commit/' to go to specific commit





