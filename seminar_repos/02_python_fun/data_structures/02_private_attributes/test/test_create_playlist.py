from src.create_playlist import CreatePlaylist


class TestProperties:
    def test_name_property(self):
        test_playlist = CreatePlaylist("playlist name")
        assert test_playlist.name == "playlist name"

    def test_tracks_property(self):
        test_playlist = CreatePlaylist("playlist name")
        assert test_playlist.tracks == []


class TestAddTrackMethod:
    def test_add_track_method_adds_track(self):
        test_playlist = CreatePlaylist("playlist name")
        test_playlist.add_track("song name")
        assert test_playlist.tracks == ["song name"]

    def test_add_track_method_adds_multiple_tracks(self):
        test_playlist = CreatePlaylist("playlist name")
        test_playlist.add_track("song name")
        test_playlist.add_track("song name 2")
        assert test_playlist.tracks == ["song name", "song name 2"]

    def test_add_track_method_returns_message(self):
        test_playlist = CreatePlaylist("playlist name")
        result = test_playlist.add_track("song name")
        assert result == "Added song name to playlist name"


class TestGetCurrentTrackMethod:
    def test_returns_current_track(self):
        test_playlist = CreatePlaylist("playlist name")
        test_playlist.add_track("song name")
        assert test_playlist.get_current_track() == "Now playing: song name"


# Implemnent
class TestNextTrackMethod:
    def test_changes_current_track_to_next_one_in_tracks(self):
        test_playlist = CreatePlaylist("playlist name")
        test_playlist.add_track("song name")
        test_playlist.add_track("song name 2")
        test_playlist.next_track()
        assert test_playlist.get_current_track() == "Now playing: song name 2"

    def test_does_not_change_track_if_end_of_playlist(self):
        test_playlist = CreatePlaylist("playlist name")
        test_playlist.add_track("song name")
        test_playlist.add_track("song name 2")
        test_playlist.next_track()
        test_playlist.next_track()

        assert test_playlist.get_current_track() == "Now playing: song name 2"
