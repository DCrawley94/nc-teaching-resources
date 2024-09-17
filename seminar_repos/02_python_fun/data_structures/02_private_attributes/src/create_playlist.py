"""
Playlist Methods:

get_current_track:
    Args: None
    Returns: String informing the user of the current tack that is playing
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

    def add_track(self, track):
        self.tracks.append(track)
        return f"Added {track} to {self.name}"
