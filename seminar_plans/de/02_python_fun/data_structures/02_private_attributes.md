# Data Structures: Private Attributes

Figjam: https://www.figma.com/board/Dn4a5dXYqID76PB6DLx2x8/OOP-2---Private-Attributes?node-id=0-1&t=uVjhJ04dc1aOeVl5-1

## Learning Objectives

- Be able to build a complex method with TDD
- Understand why we might not want to expose the full implementation of a method.

## Plan

### `get_current_track`

Explain the behaviour to students and ask what a sensible first test might be.

**they might suggest handling an empty playlist but push them away from this and assume the happy path**

- Returns name of first song in list

Anything else for now? - Not really. We might want to test if it can return the correct song when the playlist progresses but currently there's no way of progressing.

Could manually change the index tracking the position but that ties us to this implementation whereas we might want to change the implementation in the future.

```py
def get_current_track(self):
    return f"Now playing: {self.tracks[self._current_track_index]}"
```

### `next_track`

What can we test? Can we make use of previously defined methods?

- Test that when we invoked `next_track` the `get_current_track` method returns the next song in the playlist

How do we track our place in the playlist?

- some kind of current track index

Discuss attribute uses for tracking the current track - do we need to test this? Does the user of our class really need it or is it just an implementation detail?

**Comparison to functions - we don't test variables that we define inside them so why test this?**

Test:

```py
def test_changes_current_track_to_next_one_in_tracks(self):
        test_playlist = CreatePlaylist("playlist name")
        test_playlist.add_track("song name")
        test_playlist.add_track("song name 2")
        test_playlist.next_track()
        assert test_playlist.get_current_track() == "Now playing: song name 2"
```

**Possible method solutions:**

```py
def __init__(self, name):
        self.name = name
        self.tracks = []
        self._current_track_index = 0

def next_track(self):
        return self._current_track_index += 1

```

What if we get to the end of the list?

The behaviour I want is that current track won't increase if there are no more songs (not realistic but good enough for our purposes)

Test:

```py
def test_does_not_change_track_if_end_of_playlist(self):
        test_playlist = CreatePlaylist("playlist name")
        test_playlist.add_track("song name")
        test_playlist.add_track("song name 2")
        test_playlist.next_track()
        test_playlist.next_track()

        assert test_playlist.get_current_track() == "Now playing: song name 2"
```

Possible solution:

```py
def next_track(self):
        if self._current_track_index < len(self.tracks) - 1:
            self._current_track_index += 1
```
