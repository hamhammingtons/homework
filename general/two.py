result = []


def divider(a, b):
    if a < b:
        raise ValueError("num 'a' < 'b'")
    if b > 100:
        raise IndexError("num 'b' > 100")
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(int(key), data[key])
        result.append(res)
    except Exception as e:
        print(f"err: {type(e).__name__} — {e}")

print(f"err: {result}")
