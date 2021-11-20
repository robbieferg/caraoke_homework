import unittest
from classes.room import Room
from classes.song import Song
from tests.song_test import *

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song_2 = Song("Don't Stop Believing", "Journey", 4.11)
        self.song_3 = Song("Pinball Wizard", "The Who", 2.57)
        self.song_4 = Song("Ocean Man", "Ween", 2.07)
        self.song_5 = Song("Mississippi Queen", "Mountain", 2.30)
        self.song_6 = Song("Dancing Queen", "Abba", 3.52)
        self.song_7 = Song("Sweet Caroline", "Neil Diamond", 3.21)
        self.song_8 = Song("Don't Stop Me Now", "Queen", 3.29)
        self.song_9 = Song("Wannabe", "Spice Girls", 2.52)
        self.room_1 = Room(1, 12, [self.song_2, self.song_4, self.song_6])


    def test_room_has_number(self):
        expected = 1
        actual = self.room_1.room_number
        self.assertEqual(expected, actual)

    def test_room_capacity(self):
        expected = 12
        actual = self.room_1.capacity
        self.assertEqual(expected, actual)

    def test_room_has_playlist(self):
        self.assertIn(self.song_2, self.room_1.playlist)
        self.assertIn(self.song_4, self.room_1.playlist)
        self.assertIn(self.song_6, self.room_1.playlist)

    def test_room_can_add_song(self):
        self.room_1.add_song_to_playlist(self.song_3)
        self.assertIn(self.song_3, self.room_1.playlist)

    def test_room_can_remove_song(self):
        self.room_1.add_song_to_playlist(self.song_5)
        self.room_1.remove_song_from_playlist(self.song_5)
        self.assertNotIn(self.song_5, self.room_1.playlist)