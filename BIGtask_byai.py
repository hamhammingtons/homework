authorized = {"ale", "mo", "bobo", "f", "some_guy"}
blacklisted = {"badguy", "someGaf"}

safety_training = {"ale", "mo", "eye"}

security_log: list[tuple] = [("Alice", "Lab", "00:90"), ("badguy", "lab", "125421")]

simplified = [k[0] for k in security_log]

for people in simplified:
    if people in blacklisted:
        print(f'very bad, the guy "{people}" is blacklisted')
    elif people in authorized:
        for k in security_log:
            name = k[0]
            place = k[1]
            time = k[2]
            print(f"access granted to {place} for {place} at {time}")
    else:
        print(
            f"the user {people} isnt blacklisted but not permitted to use the zone at all"
        )

print(
    authorized.difference(safety_training), "havent completed training"
)  # how safety training differs from authorized

print(
    safety_training.intersection(authorized), "authorized and done training"
)  # who is authorized and done training
