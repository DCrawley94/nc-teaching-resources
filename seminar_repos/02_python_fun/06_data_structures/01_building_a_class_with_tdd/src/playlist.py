class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    # TODO: add_track
    def add_track(self, track="Never Gonna Give You Up"):
        self.tracks.append(track)
        return f"Added {track} to {self.name}"

    # TODO: get_current_track

    # TODO: next_track


"""
# Behaviour:

playlist = Playlist("Party Playlist")

playlist.name 
# "Party Playlist"
playlist.tracks 
# []

playlist.add_track("Firestarter") 
# returns: "Added Firestarter to Party Playlist"

playlist.tracks 
# ["Firestarter"]

playlist.add_track() 
# returns: "Added "Never Gonna Give You Up to Party Playlist"
playlist.tracks 
# ["Firestarter", "Never Gonna Give You Up"]

playlist.get_current_track() 
# Returns "Now playing: Firestarter"

playlist.next_track()

playlist.get_current_track() 
# Returns "Now playing: Never Gonna Give You Up" 
"""
