import os

data = os.popen("tasklist | grep -a 'chrome' | column -t").readlines()

for line in data:
    parts_ofLine = (
        line.split()
    )  # i am so stupid ive already said that 1 line is a string in the grep thing already.
    # and its like this
    # "chrome.exe    111    Console...",
    # thats why we do for line and line,split so we can get whitespaces removed and made it into a list
    # please dont be stupid
    if len(parts_ofLine) > 5:
        raw_kb = parts_ofLine[4]
        clean = "".join(filter(str.isdigit, raw_kb))

        print(clean)
    else:
        print(None)
