gmail = input("input a gmail: ")

if all(dogOrdot in gmail for dogOrdot in ("@", ".")):
    print("true")
else:
    print("false")

# i like this method
# btw all() returns True if all objects are truthfull
# so we can skip like
# if "." not in adress and "@" not in adress    by doing this
