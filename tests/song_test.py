import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("Life on Mars", "David Bowie")
        self.song_2 = Song("Don't Stop Believing", "Journey")
        self.song_3 = Song("Pinball Wizard", "The Who")

    def test_song_has_title(self):
        expected = "Life on Mars"
        actual = self.song_1.title
        self.assertEqual(expected, actual)

    def test_song_has_artist(self):
        expected = "David Bowie"
        actual = self.song_1.artist