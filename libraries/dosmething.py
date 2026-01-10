from itertools import chain, combinations, permutations, product

# only useful thing i see from itertools i see is chain, combinations, permutations


def topointout(
    val: str,
) -> None:  # shouldve have included a \n or made it a class for simplification but ok
    try:
        print("-" * 12 + f"{val}" + "-" * 12)
    except TypeError:
        print("wrong type")
    except Exception as e:
        print(e)


d = ["d", "df"]
c = ["c", "cf"]

topointout("chain")

for i in chain(d, c):  # combines 2 lists together
    print(i)


items = ["A", "B", "C", "D"]

topointout("chain")

print("\n")

topointout("combinations")

for i in combinations(
    items, 2
):  # order deosnt matter so for example ex: a,b: a,c: a,d ||| b,a: b,c...
    var1, var2 = i
    print(f"var1: {var1}\nvar 2: {var2}", "\tnote:" + str(i), "\n")

topointout("combinations")

print("\n")

topointout("permutations")

print(
    list(permutations(items, 2))
)  # for all combinations like a nested for loop (order matters)

topointout("permutations")

print("\n")

topointout("product")

for x, y in product(
    [1, 2], ["a", "b"]
):  # you can like make 1a, 1b, 2a, 2b, pretty useful
    print(x, y)

topointout("product")


print("\n", "=" * 12 + "dont mind below")

# mini task or whatever
players = ["Alex", "Ben", "Chris", "Dan"]

for combo in combinations(players, 2):
    var1, var2 = combo
    print(var1, var2)
