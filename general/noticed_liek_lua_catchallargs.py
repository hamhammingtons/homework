n = ["dd", "gg", "vcc"]


def toexpand(*args):
    # Find the first list or tuple in args
    list_found = None
    for item in args:
        if isinstance(item, (list, tuple)):
            list_found = item
            break

    print(list_found)


toexpand(n)


# REFARCTOR THIS TO A CLASS INSTEAD
