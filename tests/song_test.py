import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("Life on Mars", "David Bowie", 3.48)
        

    def test_song_title(self):
        expected = "Life on Mars"
        actual = self.song_1.title
        self.assertEqual(expected, actual)

    def test_song_artist(self):
        expected = "David Bowie"
        actual = self.song_1.artist

    def test_song_length(self):
        expected = 3.48
        actual = self.song_1.length