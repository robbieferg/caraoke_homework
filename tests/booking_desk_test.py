import unittest
from classes.booking_desk import BookingDesk
from tests.room_test import TestRoom
from classes.room import Room
from classes.guest import Guest

class TestBookingDesk(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Brian", 360.00)
        self.guest_2 = Guest("Jane", 45.90)
        self.guest_3 = Guest("Harvey", 60.41)
        self.guest_4 = Guest("Melissa", 29.80)
        self.guest_5 = Guest("Jake", 35.50)
        self.room_2 = Room(2, 12, [])
        self.room_3 = Room(3, 9, [])
        self.room_4 = Room(4, 6, [])
        self.booking_desk = BookingDesk([self.room_2, self.room_3, self.room_4], 0.00)

    def test_booking_desk_rooms_available(self):
        self.assertIn(self.room_2, self.booking_desk.rooms_available)

    def test_booking_desk_till(self):
        expected = 0.00
        actual = self.booking_desk.till
        self.assertEqual(expected, actual)

    def test_booking_desk_price_per_person_per_hour(self):
        expected = 12.50
        actual = self.booking_desk.price_per_person_per_hour
        self.assertEqual(expected, actual)

    def test_add_money_to_till(self):
        self.booking_desk.add_money_to_till(10.00)
        expected = 10.00
        actual = self.booking_desk.till
        self.assertEqual(expected, actual)

    def test_booking_desk_make_booking__party_size_fits_1_room(self):
        self.booking_desk.make_booking(self.guest_1, [self.guest_2, self.guest_3, self.guest_4, self.guest_5], 4)

        self.assertEqual(250.00, self.booking_desk.till)
        self.assertEqual(110.00, self.guest_1.money)
        self.assertEqual([self.room_4], self.booking_desk.rooms_assigned)
        self.assertEqual(5, len(self.room_4.guests_present))

    def test_booking_desk_check_out_party(self):
        self.booking_desk.make_booking(self.guest_1, [self.guest_2, self.guest_3, self.guest_4, self.guest_5], 4)
        self.booking_desk.check_out_party(self.guest_1)
        self.assertEqual([], self.guest_1.rooms_occupied_by_guests_party)
        self.assertIn(self.room_4, self.booking_desk.rooms_available)
        self.assertNotIn(self.room_4, self.booking_desk.rooms_assigned)

