import os

file = r"howework_for_itstep\libraries\os\for_testing_purposes"
# grep [FLAGS] "SEARCH_TERM" [FILE_PATH]

os.system(f"grep -a '123' {file}")  # just so eveyrthing is converted to a string

os.system(
    f"grep -v 'fabolous' {file}"
)  # if you want everything except 1 thing, use this.    fabolous here is whats skipped

os.system(f"grep -i 'Fabolous' {file}")  # use this for ignoring case sensetivity
print("\n cool starts here \n")
os.system(
    f"cat {file} | column -t"
)  # cool thing, its for like making comprehensive text: (LOOK BELOW)

# example:
# hello           there  im     alex
# this            is     quite  spontanteous

os.system(
    f'grep -E "fabolous|quite" {file}'
)  # for some reason, the SEARCH_TERM must be in dobule quotes, not single, then it works. so 'body "SEARCH_TERM" ... '
os.system(f"grep 'this' {file} > test_item.txt")  # works! its for like logging purposes
# ^^^^ i was talking about this, so instead of saving output to the terminal we save it to a file using >
# so 1st part is the expressions and then we save it into the file.


# but what if we want to
# 1. find a thing inside a file using grep first, store it into a variable
# 2. do column -t on it so it looks good
messy_data = "ID Name Department\n1 Alice Engineering\n2 Bob HR"

# This creates the file 'note.txt' with the formatted table
os.system(f'echo "{messy_data}" | column -t > note.txt')

print("Table saved to note.txt!")
# no works, fix tommorw
# TODO: do the thing we want to do "but what if we want to..."
