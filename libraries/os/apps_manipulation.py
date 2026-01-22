# ive already done os.startfile() but i just want to review how we can manipulate apps doing this
import os

# os.startfile("notepad.exe")

# os system is a bit different you can actually manipulate things using it, but you need to know cmd
# we can use f strings with .system() so ill just do this instead
folder_path = r"howework_for_itstep\libraries\os"

print(os.system("pwd"))  # Print Working Directory == os.getcwd
print(os.system(f"ls {folder_path}"))  # List the contents of your specific folder

# os.system("cd")  # changes directory but this doesnt work for some reason
# ^ Note from ai: os.system opens a temrinal. Doin this opens a new terminal. 2. It moves back one folder. 3. The terminal closes. 4.
# Your Python script is still sitting in the original folder. 'use chdir instead'

# FIXED: We tell 'cp' exactly where the file is
os.system(f"cp {folder_path}\\test_item {folder_path}\\test_item_backup")  # cp = copy
# ok so i guess the second argument must be a new name for the item with
# directory/new_name or whatever
# also if youre going to create/delete a folder use -r

# -----------------------------------
# \\ is used for a literal backslash btw
# ^^^^^^^^^^^^^^^^^^^^^^^^^

os.system(
    f"cat {folder_path}\\test_item"
)  # cat = concatenate - peek insides of the file [in terminal]

os.system(
    f"cat {folder_path}\\test_item | grep 'nothing'"
)  # grep = Global Regular Expression Print [global regex print]
os.system(f"cat {folder_path}\\test_item | grep 'XYZ'")  # works too

# ^^ i dont like this. its very messy. becuase both cat and the grep are outputted at the same line.
# we can do just grep instead.

# ^ ALSO i am a bit wrong. lets say we want to check the output of a command.
# we can do for example: tasklist | grep "notepad" to not get full data and only sort by what we need, here- notepad
# grep is like an extra parameter which is cool for sorting things out
print("\n", "- heres where simple syntax starts")

os.system(
    r"grep --color 'XYZ' howework_for_itstep\libraries\os\test_item"
)  # now this is cool for file searching ONLY
# i also like --color because it only highlights the XYZ if found

os.system("tasklist | grep 'notepad.exe'")

# so how to use grep
# imagine if we have a big chunk of data (like 10 gb) and when we do cat, cat streams that data, meaning
# it will print out EVERYTHING
# but if we want to extract only some data we can use grep with your flag.
# we need to use | which is a pipe to do this (as ive played the roblox game town it is used for doing multiple things but idk if its relevant)
# btw cat is line by line, grep looks at that line and if it has the flag (ex. str) then it gets it, if not then doesnt do anything about it

# also new thing: .txt extension mention isnt really needed apparently so uhh you can do without .txt
