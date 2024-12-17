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

test_playlist = Playlist("Party Playlist")

test_playlist.name # "Party Playlist"
test_playlist.tracks # []

test_playlist.add_track("Firestarter") # returns: "Added Firestarter to Party Playlist"
test_playlist.tracks # ["Firestarter"]

test_playlist.add_track() # returns: "Added "Never Gonna Give You Up to Party Playlist"
test_playlist.tracks # ["Firestarter", "Never Gonna Give You Up"]

test_playlist.get_current_track() # Returns "Now playing: Firestarter"

test_playlist.next_track()

test_playlist.get_current_track() # Returns "Now playing: Never Gonna Give You Up"
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
