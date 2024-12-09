from src.playlist import Playlist


class TestProperties:
    def test_name_property(self):
        test_playlist = Playlist("playlist name")
        assert test_playlist.name == "playlist name"

    def test_tracks_property(self):
        test_playlist = Playlist("playlist name")
        assert test_playlist.tracks == []


class TestAddTrackMethod:
    def test_add_track_method_adds_track(self):
        test_playlist = Playlist("playlist name")
        test_playlist.add_track("song name")
        assert test_playlist.tracks == ["song name"]

    def test_add_track_method_adds_multiple_tracks(self):
        test_playlist = Playlist("playlist name")
        test_playlist.add_track("song name")
        test_playlist.add_track("song name 2")
        assert test_playlist.tracks == ["song name", "song name 2"]

    def test_add_track_method_returns_message(self):
        test_playlist = Playlist("playlist name")
        result = test_playlist.add_track("song name")
        assert result == "Added song name to playlist name"


class TestGetCurrentTrack:
    def test_get_current_track_returns_string_with_first_song(self):
        # Arrange
        test_playlist = Playlist("test playlist")
        test_playlist.add_track("Song 2")
        expected_output = "Now playing: Song 2"

        # Act
        result = test_playlist.get_current_track()

        # Assert
        assert result == expected_output

        test_playlist_2 = Playlist("test playlist")
        test_playlist_2.add_track("Amazing Grace")
        expected_output_2 = "Now playing: Amazing Grace"

        # Act
        result_2 = test_playlist_2.get_current_track()

        # Assert
        assert result_2 == expected_output_2

    def test_get_current_track_return_empty_playlist_message(self):
        test_playlist = Playlist("Andrew's Playlist")

        expected_output = "Playlist is empty!"

        assert test_playlist.get_current_track() == expected_output


class TestNextTrack:
    def test_next_track_moves_forward_in_the_playlist(self):
        test_playlist = Playlist("Joseph's Playlist")
        test_playlist.add_track("Beethoven 9")
        test_playlist.add_track("Sandstorm")

        expected_output = "Now playing: Sandstorm"

        test_playlist.next_track()

        assert test_playlist.get_current_track() == expected_output

    def test_next_track_does_not_move_forward_after_the_final_song(self):
        test_playlist = Playlist("Joseph's Playlist")
        test_playlist.add_track("Beethoven 9")
        test_playlist.add_track("Sandstorm")

        expected_output = "Now playing: Sandstorm"

        test_playlist.next_track()
        test_playlist.next_track()
        test_playlist.next_track()
        test_playlist.next_track()

        assert test_playlist.get_current_track() == expected_output
