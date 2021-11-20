class Guest:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def pay_money(self, amount):
        self.money -= amount
        