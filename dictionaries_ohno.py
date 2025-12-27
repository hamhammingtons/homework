thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

newdic = {}


class Things:  # should have specified that thisdic would be a changed_dic in an __init__ because i gotta do it manualy now
    def ToPrint(self, changed_dic):
        print(changed_dic)

    def ToCheck(self, dic, key):
        if key in dic:
            return True
        else:
            return False

    def ToChangeValue(self, dic, key, value):
        dic[key] = value

    def ToUnion(self, onedic: dict, twodic: dict):
        onedic.update(twodic)
        print(onedic)

    def ToUpdateValue(self, dic: dict, key, value):
        if key in dic:
            dic.update({key: value})
        else:
            print("value not found, adding a new one")
            dic.update({key: value})

    def ToDeleteKey(self, dic: dict, key):
        dic.pop(key)

    def ToDeleteLastItem(self, dic: dict):
        dic.popitem()  # deletes last added item

    def ToReturnKeysAndValuesAndItemsInaForLoop(self, dic: dict):
        for k in dic.keys():
            print(k)

        for x in dic.values():
            print(x)

        for key, value in dic.items():
            print(key, value)

    def Tocopy(self, dic, dic2):
        dic2 = dict(dic)


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
