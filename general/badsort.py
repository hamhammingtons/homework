class Solution:
    def Tofix(self, list: list, target: int):
        for index in range(len(list)):
            if list[index] > 100:
                return index
        return -1
