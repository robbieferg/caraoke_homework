class Room:
    def __init__(self, room_number, capacity, playlist):
        self.room_number = room_number
        self.capacity = capacity
        self.playlist = playlist
        self.guests_present = []

    def add_song_to_playlist(self, song):
        self.playlist.append(song)

    def remove_song_from_playlist(self, song):
        self.playlist.remove(song)