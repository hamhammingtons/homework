import random


class DataVault:
    def __init__(self, *numbers):
        self.__numbers = numbers

    def get_numbers(self):
        return self.__numbers


class Encryptor(DataVault):
    def __init__(self, *numbers):
        super().__init__(*numbers)
        self.__result = self.__calculate()

    def __calculate(self):
        nums = self.get_numbers()
        if not nums:
            return 0

        op = random.choice(["+", "*", "-"])
        res = nums[0]
        for n in nums[1:]:
            if op == "+":
                res += n
            elif op == "*":
                res *= n
            elif op == "-":
                res -= n
        return res

    def __str__(self):
        return f"resultse: {self.__result}"


secret = Encryptor(10, 2, 5)
print(secret)
