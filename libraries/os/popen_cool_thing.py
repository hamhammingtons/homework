import os

# ok so i get how popen works it just opens up powershell in like a side window but not visible to the user and then
# we can manipulate the output by doing popen which is really cool

CMD_INPUT = os.popen("whoami").read()
# ^ problem: outputs everything. if we have lot of data this will suck
print(CMD_INPUT)

lines = os.popen("ls").readlines()  # returns a list, baaaasically like .split()
print(lines)

with os.popen("tasklist") as pipe:  # this costs 0 kb for our computer, most efficient
    for line in pipe:
        count = 0
        if "chrome.exe" in line:
            print(f"Found a Chrome process!")

print("\n")

with os.popen(
    "tasklist | grep -a 'chrome.exe'"
) as CHROME_PIPE:  # big string with every instance of chrome exe.
    total_kb = 0

    for line in CHROME_PIPE:  # we do for here to go thru each line of the pipe
        item_inst = line.split()
        if len(item_inst) >= 5:
            # item_inst[4] is the '248я084' part
            dirty_mem = item_inst[4]

            # CLEANING TRICK: Keep only the digits 0-9
            # We filter the string and join only the numbers back together
            clean_mem = "".join(filter(str.isdigit, dirty_mem))

            if clean_mem:  # Make sure it's not empty
                total_kb += int(clean_mem)
                print(f"Found Chrome Process: {clean_mem} KB")

print("-" * 30)
print(f"Total Memory: {total_kb:,} KB")
