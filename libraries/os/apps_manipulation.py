# ive already done os.startfile() but i just want to review how we can manipulate apps doing this
import os

# os.startfile("notepad.exe")

# os system is a bit different you can actually manipulate things using it, but you need to know cmd

print(os.system("pwd"))  # Print Working Directory == os.getcwd
print(os.system("ls"))  # List = os.listdir()
# os.system("cd")  # changes directory but this doesnt work for some reason
# ^ Note from ai: os.system opens a temrinal. Doin this opens a new terminal. 2. It moves back one folder. 3. The terminal closes. 4.
# Your Python script is still sitting in the original folder. 'use chdir instead'

os.system(
    r"cp test_item.txt howework_for_itstep\libraries\os"
)  # cp = copy, doesnt work

os.system(
    r"cat howework_for_itstep\libraries\os\test_item"
)  # cat = concatenate - peek insides of the file [in terminal]

os.system(
    r"cat howework_for_itstep\libraries\os\test_item | grep 'Nothing'"
)  # grep = Global Regular Expression Print [global regex print]

# so how to use grep
# imagine if we have a big chunk of data (like 10 gb) and when we do cat, cat streams that data, meaning
# it will print out EVERYTHING
# but if we want to extract only some data we can use grep with your flag.
# we need to use | which is a pipe to do this
# btw cat is line by line, grep looks at that line and if it has the flag (ex. str) then it gets it, if not then doesnt do anything about it
