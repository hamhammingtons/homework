import os
from datetime import datetime

print(os.stat(r"howework_for_itstep\libraries\os\test_item"))

# --- stat result notes and stuff  ---
# st_mode  = Permissions & file type
# st_ino   = Inode (The file's unique ID/address on the disk)
# st_dev   = Device ID (Which drive the file is on) -- more explicit- on which Disk Partition the file is on.
# ^ A bit complicated, but imagine if we are going to have 2 boot options (os):
#   Were gona split our 500gb data drvie into 2 parts:
#   120 gb for Linux, 360 gb for Windows
#   Now, we have partitioned the drive into 2 parts. and st_dev shows us on which partition the file is in

# st_nlink = Number of hard links (How many "pointers" point to this data)
# ^ for context, there are Soft Links (which is a pointer to an another pointer to data) (filenames to be explicit)
#   and Hard Links (multiple pointers to data (names))
#
# st_uid   = User ID of owner (like str type converted to bytes, then it converts itself into str so people can understnad)
# st_gid   = Group ID of owner (like if a company owns this file, it is restricted for them, but for the CEO he can access to whatever)
# st_size  = Size of file in BYTES
# st_atime = Last Access Time (seconds since Jan 1, 1970)
# st_mtime = Last Content Modification Time
# st_ctime = Last Metadata Change Time (Windows) or Creation Time
# ------------------------------- ^ i like dis -----------------------------


# ----------------------hypothosis part----------------------- #

# stat has its own attributes so for example os.stat without anything returns every data about the file if we want its size we will do
path = os.stat(r"howework_for_itstep\libraries\os\test_item").st_mtime
print(datetime.fromtimestamp(path))


# -------- new methods---------- #
# os.walk()  basically like listdir but if you would like to yield (meanign saving memory) the objects and also return everything
#            starting from the top folder (ex. \os\test_item) - test_item is the top folder here.
#            it will list eveyrthing in that folder, whatever exists in it.

mypath = r"howework_for_itstep\libraries\os"  # note: do not include a filename as the top folder it will not work sir

for directory_path, directory_names, file_names in os.walk(mypath):
    print(
        f'Directory path: {directory_path},\n "directory names: {directory_names} \n "filenames: {file_names}'
    )

# 12 : 18 stopped wathching
