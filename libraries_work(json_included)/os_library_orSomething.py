import os

newfiles = {}  # should it be a set or a dictionary?

for i in range(1, 3):  # makse 2 files in the same folder
    changed = f"name_{i}"  # this is useful
    os.mkdir(changed)
    path = os.path.abspath(changed)

    newfiles[changed] = path

    os.rmdir(changed)
print(newfiles)  # works
