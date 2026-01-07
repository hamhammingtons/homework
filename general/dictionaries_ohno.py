thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

newdic = {}


class Things:
    class Things:
        def __init__(self, dic):  # fixed this ^^^^
            self.dic = dic

        def ToPrint(self):
            print(self.dic)

        def ToCheck(self, key):
            return (
                key in self.dic
            )  # no need for printing true or false because it reutrns it already

        def ToChangeValue(self, key, value):
            self.dic[key] = value

        def ToUnion(self, other_dic: dict):
            self.dic.update(other_dic)
            print(self.dic)

        def ToUpdateValue(self, key, value):
            if key not in self.dic:
                print("Value not found, adding a new one")
            self.dic.update({key: value})

        def ToDeleteKey(self, key):
            # pop() returns the value, but here we just use it to delete
            self.dic.pop(key)

        def ToDeleteLastItem(self):
            self.dic.popitem()

        def ToReturnAll(self):
            for k in self.dic.keys():
                print(f"Key: {k}")
            for v in self.dic.values():
                print(f"Value: {v}")
            for k, v in self.dic.items():
                print(f"Item: {k} -> {v}")

        def ToCopy(self):
            # This returns a fresh copy of the dictionary
            return self.dic.copy()


nested = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}

print(nested["child1"]["name"], "------dont mind")

# if you are looking for both k and values, in this we are only looking for values

for k, v in nested.items():
    for name, year in v.items():
        print(name, year)

# my example because i dont need keys
for v in nested.values():
    print("--------my ex statrs jere-----------")
    for name, year in v.items():
        print(name, year)
