class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []
        self.curr_track_index = 0

    def add_track(self, track="Never Gonna Give You Up"):
        self.tracks.append(track)
        return f"Added {track} to {self.name}"

    def get_current_track(self):
        return f"Now playing: {self.tracks[self.curr_track_index]}"

    def next_track(self):
        self.curr_track_index += 1

    # TODO: add_track

    # TODO: get_current_track

    # TODO: next_track
