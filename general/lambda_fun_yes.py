def f(number):
    print(f"last number number: {number}")
    return lambda a: a * number


double = f(
    2
)  # double is now a function of f, where f.number = 2. we Assgined the value.
print(
    double(3)
)  # when we call double, since its a func with number as 2, it need a, so it does a as 3. 3*2 = 6
print(double(2))  # same thing here. 2: 2*2 = 4

# this means that with this we can essenteatilly do something like a "class" method but cheaper.

triple = f(3)
print(triple(3), "-" * 3, "new var of triple")  # 3*3


# now for the cool stuff

normal = [1, 2, 3, 4]

sqr = list(map(lambda iterable: iterable**2, normal))
#  ^^^ we need to include the list itself at the end ["...**2, list <---"]
print(
    sqr
)  # so map is an alternative to iteration via for loops, it does the same thing.

filtered = list(filter(lambda iterable: iterable % 2 == 0, normal))
print(
    filtered
)  # same thing, its for iteration, but it instead filter out if the condition in the expression is met.

filtered = None


people = [("Alice", 30), ("Bob", 20), ("Charlie", 25)]

sorted_age_extracted = [k[1] for k in sorted(people, key=lambda x: x[1])]
"""
explanation: we first sort the people by ages using lambda x: x[1] where x is a tuple.
then we get the index of 1, which is the age value of x(tuple), using k[1] for k in sorted(...)

Sorted() here is used to sort the elements, im not exactly sure on how key works here but its like 'to change a pattern'
"""
print(sorted_age_extracted)
