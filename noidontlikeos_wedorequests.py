import requests, json  # type: ignore

ummm = []

for i in range(1, 6):
    reps = requests.get(f"https://jsonplaceholder.typicode.com/todos/{i}")
    data = reps.json()
    ummm.append(data)

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
