class Guest:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.rooms_occupied_by_guests_party = []
        

    def pay_money(self, amount):
        self.money -= amount
        