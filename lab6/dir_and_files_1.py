import os

path = '.'

all_items = os.listdir(path)

print("All items:", all_items)

print("\nDirectories:")
for item in all_items:
    if os.path.isdir(item):
        print(item)

print("\nFiles:")
for item in all_items:
    if os.path.isfile(item):
        print(item)