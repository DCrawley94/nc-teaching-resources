import pytest

# This function should take a string representing a time with hours and
#  minutes separated by a colon e.g. "13:25"
# Some of the times are written in the 24-hour clock format
# This function should return the time written in the 12-hour clock format


def convert_time_string(string):
    pass


def test_convert_time_string_returns_the_string_unchanged_if_already_within_the_right_format():
    assert convert_time_string("06:28") == "06:28"


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_convert_time_string_converts_an_afternoon_time_to_the_12_hour_format():
    assert convert_time_string("16:07") == "04:07"


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_convert_time_string_converts_times_in_the_hour_after_midnight_to_the_12_hour_format():
    assert convert_time_string("00:56") == "12:56"
    assert convert_time_string("00:00") == "12:00"
