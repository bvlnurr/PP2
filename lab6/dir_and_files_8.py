import os

path = 'example.txt'

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print(f"{path} deleted.")
    else:
        print("No permission to delete the file.")
else:
    print("File does not exist.")