here = (2, 3, 4)


def tochange(tup: tuple):
    new = list(tup)
    new[-1] *= 2
    tup = tuple(new)

    return tup


print(tochange(here))
