import os
import shutil  # Added for the "Delete Everything" comparison

# --- ABBREVIATIONS ---
# chdir     = change directory
# rename    = rename a file (old_name, new_name) ALL STRINGS
# cwd       = current working directory (use case - getcwd())
# mkdir     = Make Directory
# makedirs  = Make Directories (plural/recursive)
# rmdir     = Remove Directory
# removedirs = Remove Directories (plural/recursive)
# listdir   = List Directory contents

# ----------------------hypothosis part----------------------- #


# 1. CREATION
#   mkdir: Creates exactly ONE folder. If the parent doesn't exist, it crashes.
os.mkdir("Demo")


# makedirs: Creates the whole path (folders inside folders).
#   'Hello' is created first, then 'World' is created inside it.
os.makedirs("Hello/World", exist_ok=True)


# 2. THE "NOTES" CASE (Preparation)
#   Let's put a file in 'Hello' to see how it affects removal later.
with open("Hello/note.txt", "w") as f:
    f.write("file to prevent deletion.")


# 3. LISTING
#   listdir: Shows what is inside a folder (returns a list of strings).
print(f"Contents of CWD: {os.listdir()}")
print(f"Contents of Hello: {os.listdir('Hello')}")


# 4. REMOVAL

#   4.1 rmdir: Removes exactly ONE empty folder.
os.rmdir("Demo")


#   4.2 removedirs: The "Recursive" remover.
# Logic:
# 1. It tries to delete 'World'. (Success, it's empty).
# 2. It moves up to 'Hello'.
# 3. It sees 'note.txt'. It stops and leaves 'Hello'.
try:
    os.removedirs("Hello/World")
    print("removedirs finished its attempt.")
except OSError:
    print("Could not delete because folder not empty.")


# 5. FINAL CHECK
if os.path.exists("Hello"):
    print("Parent 'Hello' is still here because of the file inside.")


os.chdir("Hello")  # make sure to change directory before changing anything
os.rename("note.txt", "HelloHello.txt")

# TODO: i went to bed after the '5:46' mark of the video 'https://www.youtube.com/watch?v=tJxcKyFMTGo' so continue watching it tommorow
