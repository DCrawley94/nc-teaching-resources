# Building Classes with TDD

## Learning Objectives

- Know how to test attributes on a class instance
- Know how to create methods on a class
- Know how to test methods with TDD
- Know how to access attributes with `self`

## Warm Up

- What is a class? From the docs:

  > **Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made.**

- What is a class made up of?
  - attributes
  - methods

## Task

Each playlist should have the following attributes:

- name: list of strings
- tracks: string

And these methods:

- add_track
- get_current_track
- next_track

```py
# Behaviour:

playlist = Playlist("Party Playlist")

playlist.name # "Party Playlist"
playlist.tracks # []

playlist.add_track("Firestarter") # returns: "Added Firestarter to Party Playlist"
playlist.tracks # ["Firestarter"]

playlist.add_track() # returns: "Added "Never Gonna Give You Up to Party Playlist"
playlist.tracks # ["Firestarter", "Never Gonna Give You Up"]

playlist.get_current_track() # Returns "Now playing: Firestarter"

playlist.next_track()

playlist.get_current_track() # Returns "Now playing: Never Gonna Give You Up"
```

## Start

```py
class Playlist:
    pass

    # TODO: attributes

    # TODO: add_track

    # TODO: get_current_track

    # TODO: next_track

```

## Possible Solution

```py
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
```

## Tests

```py
# Test Attributes


class TestPlaylistAttributes:
    def test_name(self):
        test_playlst = Playlist("Geoff")

        assert test_playlst.name == "Geoff"

    def test_tracks(self):
        test_playlst = Playlist("Geoff")

        assert test_playlst.tracks == []


#  Test Methods
class TestAddTrack:
    def test_returns_formatted_string(self):
        test_playlst = Playlist("Geoff")

        result = test_playlst.add_track("Firestarter")

        assert result == "Added Firestarter to Geoff"
        assert test_playlst.tracks == ["Firestarter"]

    def test_default_song(self):
        test_playlst = Playlist("Geoff")

        result = test_playlst.add_track()

        assert result == "Added Never Gonna Give You Up to Geoff"
        assert test_playlst.tracks == ["Never Gonna Give You Up"]

    def test_multiple_tracks(self):
        test_playlst = Playlist("Geoff")

        test_playlst.add_track("Firestarter")
        test_playlst.add_track("Breathe")
        test_playlst.add_track("Out of Space")

        assert test_playlst.tracks == ["Firestarter", "Breathe", "Out of Space"]


class TestGetCurrentTrack:
    def test_returns_formatted_now_playing_string_for_current_song(self):
        test_playlist = Playlist("playlist name")
        test_playlist.add_track("song name")
        assert test_playlist.get_current_track() == "Now playing: song name"


class TestNextTrack:
    def test_moves_playlist_one_track_along(self):
        test_playlist = Playlist("Party Playlist")

        test_playlist.add_track("Firestarter")
        test_playlist.add_track("Breathe")
        test_playlist.add_track("Out of Space")

        assert test_playlist.get_current_track() == "Now playing: Firestarter"

        test_playlist.next_track()

        assert test_playlist.get_current_track() == "Now playing: Breathe"
```
