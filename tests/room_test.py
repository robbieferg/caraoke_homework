import unittest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song_2 = Song("Don't Stop Believing", "Journey", 4.11)
        self.song_3 = Song("Pinball Wizard", "The Who", 2.57)
        self.song_4 = Song("Ocean Man", "Ween", 2.07)
        self.song_5 = Song("Mississippi Queen", "Mountain", 2.30)

        self.room_1 = Room(1, 12, [self.song_2, self.song_3, self.song_5])

    def test_room_has_number(self):
        expected = 1
        actual = self.room_1.room_number
        self.assertEqual(expected, actual)

    def test_room_has_free_spaces(self):
        expected = 12
        actual = self.room_1.free_spaces
        self.assertEqual(expected, actual)

    def test_room_has_playlist(self):
        self.assertIn(self.song_2, self.room_1.playlist)
        self.assertIn(self.song_3, self.room_1.playlist)
        self.assertIn(self.song_5, self.room_1.playlist)