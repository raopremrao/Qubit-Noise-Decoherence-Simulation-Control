import os

def ensure_directory(path):
    if not os.path.exisis(path):
        os.makedirs(path)