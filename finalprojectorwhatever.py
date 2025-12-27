import random

passing_grade = 65
class_name = "8G"

students = ["John", "Alex", "Robert", "John"]

students = list(dict.fromkeys(students))  # i stole this because idk this method

record = {}

for names in students:  # did the key and value thing
    scores = (random.randint(50, 100), random.randint(50, 100))
    record[names] = scores

for k, v in record.items():
    total = (v[0] + v[1]) / 2  # supposed to be + not -
    print(f"{k} - average: {total}")
    if total >= passing_grade:
        print(f"{k} passed")
    else:
        print(f"{k} didnt pass")

print("-------------- new section ------------------")

inventory = {"Apples": (10, 1.50)}  # (Quantity, Price)

while True:
    print("\nOptions: open, add, sell, exit")
    choice = input("Select option: ").lower()

    if choice == "open":
        print("\n--- Current Inventory ---")
        for item, data in inventory.items():
            qty, price = data  # Unpacking the tuple
            print(f"Item: {item} | Qty: {qty} | Price: ${price}")

    elif choice == "add":
        try:
            item = input("Enter item name: ")
            qty = int(input("Enter quantity: "))
            price = float(input("Enter price: "))

            # Storing them as a tuple
            inventory[item] = (qty, price)
            print(f"Added {item} to inventory.")
        except ValueError:
            print("Error: Quantity must be an int and Price must be a number.")

    elif choice == "sell":
        item = input("What do you want to sell? ")
        if item in inventory:
            qty_to_sell = int(input(f"How many {item} to sell? "))
            current_qty, current_price = inventory[item]

            if qty_to_sell <= current_qty:
                # Update the quantity but keep the same price
                new_qty = current_qty - qty_to_sell
                inventory[item] = (new_qty, current_price)
                print(
                    f"Sold {qty_to_sell} {item}. Total price: {qty_to_sell * current_price}"
                )
            else:
                print("Not enough stock!")
        else:
            print("Item not found.")

    elif choice == "exit":
        break


"""
Note: this wasnt written by me, by ai, but i undersntand how this works. 

My problem was that i realized that he wanted me to do quantity, and i didnt want to refarctor it. So for example in my initial code it
just did the value and key, but in here i was asked to do a tuple of 
(quantity, value). 
This doesnt dissapoint me however because i understand how this works."""
