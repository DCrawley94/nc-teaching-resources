from src.playlist import Playlist

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
