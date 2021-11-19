import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room(1, 12)

    def test_room_has_number(self):
        expected = 1
        actual = self.room_1.room_number
        self.assertEqual(expected, actual)

    def test_room_has_free_spaces(self):
        expected = 12
        actual = self.room_1.free_spaces
        self.assertEqual(expected, actual)