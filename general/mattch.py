item = {"category": "fruit", "details": {"name": "apple", "price": 1.50}}

match item:
    case {"category": "fruit", "name": "apple", "price": sd}:
        print("the price is" + str(sd))
