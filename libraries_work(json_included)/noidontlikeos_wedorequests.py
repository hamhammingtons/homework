import requests, json  # type: ignore

# 1. The Address (A string)
address = "https://jsonplaceholder.typicode.com/todos/1"

# 2. The Data to send
payload = {"title": "I've mastered something", "completed": True}

# 3. The Action
# We pass the 'address' string and the 'payload' dictionary
response = requests.put(address, json=payload)

# 4. Check the result
# The server sends back the VERSION of the data that now "exists" on its side
updated_data = response.json()

with open("data.json", "w") as f:
    json.dump(updated_data, f, indent=4)

print("Check data.json! It should show your new title.")
