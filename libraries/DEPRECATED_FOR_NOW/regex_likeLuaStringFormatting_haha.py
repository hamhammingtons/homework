import re as regex

print("started", "\n")

digits = "123 173481 32591"

# 1. Use \d+ to actually find the first group of numbers
match = regex.search(r"\d+", digits)
if match:
    print(f"First number found: {match.group()}")

first = regex.sub(r"[^\d]", "bad", digits)
print(first)

# TODO: learn formatting i am so confused with this
