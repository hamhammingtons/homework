x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)  # stores the dupes only in 2 lists. X is the main, Y is the comparison

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(
    y
)  # stores differences, x is the main, y is the comparison.  (only checks what x differs from y)

print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)  # method keeps all items EXCEPT the duplicates.

print(z)
