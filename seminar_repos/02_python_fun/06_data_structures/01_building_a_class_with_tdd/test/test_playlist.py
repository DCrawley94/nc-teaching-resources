from src.playlist import Playlist


class TestPlaylistAttributes:
    def test_playlst_has_name_attribute(self):
        test_playlist = Playlist("Party Playlist")

        assert test_playlist.name == "Party Playlist"

    def test_playlist_has_tracks_attribute(self):
        test_playlist = Playlist("Party Playlist")

        assert test_playlist.tracks == []


class TestAddTrack:
    # Test return value: "Added Firestarter to Party Playlist"
    def test_returns_confirmation_of_added_song(self):
        test_playlist = Playlist("Party Playlist")

        result = test_playlist.add_track("Bee Gees - Tragedy")

        assert result == "Added Bee Gees - Tragedy to Party Playlist"

    # Test appends song to track list
    def test_adds_track_to_track_list(self):
        test_playlist = Playlist("Party Playlist")

        test_playlist.add_track("Orbital - Dirty Rat")

        assert test_playlist.tracks == ["Orbital - Dirty Rat"]

    # Test default song added
    def test_adds_default_track_when_none_specified(self):
        test_playlist = Playlist("Party Playlist")

        result = test_playlist.add_track()

        assert result == "Added Never Gonna Give You Up to Party Playlist"
        assert test_playlist.tracks == ["Never Gonna Give You Up"]
