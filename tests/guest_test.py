import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Brian", 76.65)

    def test_guest_has_name(self):
        expected = "Brian"
        actual = self.guest_1.name
        self.assertEqual(expected, actual)

    def test_guest_has_money(self):
        expected = 76.65
        actual = self.guest_1.money
        self.assertEqual(expected, actual)
    
