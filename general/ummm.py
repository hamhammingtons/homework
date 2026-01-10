# # we need to generate a thing
import itertools

# people = {"F", "b", "c"}
# nums = [k for k in range(1, len(people) + 1)]

# print(nums)

# fixed = [f"{x}:{y}" for x, y in itertools.product(nums, people)]

# print(fixed)

# participants = ["Alice", "Bob", "Charlie", "Dave", "Eve"]

# for giver, reciver in itertools.permutations(participants, 2):
#     print(giver, reciver)

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
