import itertools

people = {"F", "b", "c"}
nums = [k for k in range(1, len(people) + 1)]

print(nums)

fixed = [f"{x}:{y}" for x, y in itertools.product(nums, people)]

print(fixed)

participants = ["Alice", "Bob", "Charlie", "Dave", "Eve"]

for giver, reciver in itertools.permutations(participants, 2):
    print(giver, reciver)

prices = {
    "Laptop Sleeve": 30,
    "Mechanical Keyboard": 50,
    "Mouse Pad": 20,
    "USB-C Hub": 45,
    "Wireless Mouse": 25,
}

budget = 70  # lets use a for loop to scroll thru eveyrhtin and then if 1 item
affordable = []
for name, name2 in itertools.combinations(
    prices, 2
):  # actually it gets the keys only so we do prices[name]
    total = prices[name] + prices[name2]  # gets values

    if total <= budget:
        affordable.append(f"{name}+{name2}")

print(affordable)

inventory = [
    {"name": "Laptop Sleeve", "price": 30, "in_stock": True},
    {"name": "Mechanical Keyboard", "price": 50, "in_stock": False},
    {"name": "Mouse Pad", "price": 20, "in_stock": True},
    {"name": "USB-C Hub", "price": 45, "in_stock": True},
    {"name": "Wireless Mouse", "price": 25, "in_stock": False},
]

for item1, item2 in itertools.permutations(
    inventory, 2
):  # very boring method of doing this but nothing else works
    name1, price1, instock1 = item1["name"], item1["price"], item1["in_stock"]
    name2, price2, instock2 = item2["name"], item2["price"], item2["in_stock"]
    total = price1 + price2

    if total <= 70 and instock1 == True and instock2 == True:
        print(item1, item2, total)
        print("\n")
