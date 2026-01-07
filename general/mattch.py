item = {"category": "fruit", "details": {"name": "apple", "price": 1.50}}

match item:
    case {"category": "fruit", "details": {"name": "apple", "price": sd}}:  # i forgor
        print("the price is:\t" + str(sd))
