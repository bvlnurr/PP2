import os

path = 'example.txt'

if os.path.exists(path):
    print("Path exists.")
    print("Filename:", os.path.basename(path))
    print("Directory:", os.path.dirname(path))
else:
    print("path does not exists.")