import requests, json  # type: ignore

ummm = []

for i in range(1, 21):
    responce = requests.get(f"https://jsonplaceholder.typicode.com/todos/{i}")
    data = responce.json()

    if data["completed"]:
        ummm.append(data)
    else:
        print("bad data")  # this is for debugging and it actually worked
