
class BookingDesk:
    def __init__(self, rooms_available, till):
        self.rooms_available = rooms_available
        self.till = till
        self.price_per_person_per_hour = 12.50
        self.rooms_assigned = []

    def add_money_to_till(self, amount):
        self.till += amount
    
    def make_booking(self, paying_guest, additional_guests_list, num_of_hours):
        party_size = len(additional_guests_list) + 1
        total_price = self.price_per_person_per_hour * party_size * num_of_hours
        self.add_money_to_till(total_price)
        paying_guest.pay_money(total_price)

        self.rooms_available.sort(key = lambda x: x.capacity)
        for room in self.rooms_available:
            if room.capacity > party_size:
                self.rooms_assigned.append(room)
                return




        
        