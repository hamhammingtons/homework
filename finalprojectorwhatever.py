import random

passing_grade = 65
class_name = "8G"

students = ["John", "Alex", "Robert", "John"]

students = list(dict.fromkeys(students))  # i stole this because idk this method

record = {}

for names in students:  # did the key and value thing
    scores = (random.randint(50, 100), random.randint(50, 100))
    record[names] = scores

for k, v in record.items():
    total = (v[0] - v[1]) / 2
    print(f"{k} - average: {total}")
    if total > passing_grade:
        print(f"{k} passed")
    else:
        print(f"{k} didnt pass")
