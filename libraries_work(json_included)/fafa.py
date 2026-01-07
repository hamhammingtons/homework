import requests  # type: ignore
import json

# Use an endpoint that actually returns JSON data
response = requests.get("https://httpbin.org/get")

data = response.json()


with open("test.json", "w") as f:
    json.dump(data, f, indent=4)
