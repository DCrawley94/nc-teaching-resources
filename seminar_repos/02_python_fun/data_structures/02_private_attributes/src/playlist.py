"""
Playlist Methods:

get_current_track:
    Args: None
    Returns: String informing the user of the current track that is playing
            (start from the first song in the playlist).
            E.g: "Now playing: <SONG NAME>"

next_track:
    Args: None
    Returns: None

    Moves the track along in the playlist
"""


class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []
        self._current_track = 0

    def add_track(self, track):
        self.tracks.append(track)
        return f"Added {track} to {self.name}"

    def get_current_track(self):
        if not self.tracks:
            return "Playlist is empty!"
        return f"Now playing: {self.tracks[self._current_track]}"

    def next_track(self):
        if self._current_track < len(self.tracks) - 1:
            self._current_track += 1

    def _private_method(self):
        pass


playlist = Playlist("abc")
