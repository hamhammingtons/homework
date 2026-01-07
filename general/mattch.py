item = {"category": "fruit", "details": {"name": "apple", "price": 1.50}}

match item:
    case {"category": "fruit", "details": {"name": "apple", "price": sd}}:  # i forgor
        print("the price is:\t" + str(sd))


def decorator(func):
    def wrapper(*arg, **kvargs):
        print(f"--- Calling {func.__name__} ---")

        for i, a in enumerate(arg):
            match a:
                case tuple():
                    print(f"Index {i} is a tuple.")
                case dict() as d:
                    print(f"Index {i} is a dict. Merging into kvargs...")
                    kvargs.update(d)
                case list():
                    print(f"Index {i} is a list.")
                case _:
                    print(f"Index {i} is a {type(a).__name__}")

        return func(*arg, **kvargs)

    return wrapper


@decorator
def test_func(*args, **kwargs):
    print("Final Args:", args)
    print("Final Kwargs:", kwargs)


test_func(1, {"theme": "dark"}, [10, 20])
