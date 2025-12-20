"""
Поработайте над собственной симуляцией, которая должна состоять минимум из двух классов, связанных между  собой.
"""


class House:
    def __init__(self, value, bool_atr) -> None:
        self.value = value  # int
        self.bool_atr = bool_atr  # bool

    def tellValue(self):
        print(f"value {self.value}")


class Dolina:
    def __init__(self, money) -> None:
        self.money = money  # assign money

    def tocheckvalue(self, house_obj):
        if self.money < house_obj.value:  # money check
            print("i am not able to afford to buy back the house")
        else:
            print("i am gonna buy it back")

    def live(self, house_obj):
        if house_obj.bool_atr == False:
            print("i am not living in a house")
        else:
            print("i am living in a house")


the_house = House(value=901242094, bool_atr=False)
no_house = Dolina(money=134)

# connection
no_house.live(the_house)
no_house.tocheckvalue(the_house)
