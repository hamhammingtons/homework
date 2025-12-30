import requests  # type: ignore
import json

url = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data = url.json()

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
