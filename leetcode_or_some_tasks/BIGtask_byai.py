authorized = {"ale", "mo", "bobo", "f", "some_guy"}
blacklisted = {"badguy", "someGaf"}

safety_training = {"ale", "mo", "eye"}

security_log: list[tuple] = [("Alice", "Lab", "00:90"), ("badguy", "lab", "125421")]

simplified = [k[0] for k in security_log]

for name, place, time in security_log:
    if name in blacklisted:
        print(f"user is blacklisted, {name}")
    elif name in authorized:
        print(f"user is permitted. {name}")
    else:
        print(f"user is not in system, {name}")

print(
    authorized.difference(safety_training), "havent completed training"
)  # how safety training differs from authorized

print(
    safety_training.intersection(authorized), "authorized and done training"
)  # who is authorized and done training
