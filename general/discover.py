a = [[0] * 2] * 3

print(a)

a[0][1] = 1
for i in a:
    print(id(a))  # not unique.
print(a)

# the * 3 creates new lists which is a pointer to the original inside the list, so [0] * 2 is good it creates 2 copies of 0 inside the list but
# *3 puts the same object into the list thrice
print("\n")
l = [[k * j for k in range(1, 4, 2)] for j in range(1, 4)]
print(l)


def to_sum(
    a, b, c, /, *, sum_plus_minus_first: bool
):  # / goes to the left, * goes to the right
    match sum_plus_minus_first:
        case True:
            x = (a + b) * c
            return x
        case False:
            x = a + b * c
            return x


print(to_sum(3, 4, 5, sum_plus_minus_first=True))
print(to_sum(3, 4, 5, sum_plus_minus_first=False))


def to_output(func):
    def wrapper(*args, **kwargs):
        print("func called:", func.__name__)
        print(
            f"args: {len(args)}"
            if args and not kwargs
            else (
                f"kwargs: {len(kwargs)}"
                if kwargs and not args
                else (f"args: {args}, kwargs: {kwargs}" if kwargs and args else 0)
            )
        )
        return func(*args, **kwargs)

    return wrapper


@to_output
def todo(msg, **kwar):
    return "it ok sir"


print(todo("hi", ty="ok"))
# why does autocomplete do this shit
