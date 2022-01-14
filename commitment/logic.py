import os
from .verification import verify

def logic():
    branches = os.listdir(verify() + "/.git/refs/heads")


