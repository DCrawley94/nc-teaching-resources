# The statements below list the times someone spent awake / asleep over the
#  course of a 60 minute period:

# A minute 0, someone wakes up
# At minute 5, someone falls asleep
# At minute 25, someone wakes up
# At minute 30, someone falls asleep
# At minute 55, someone wakes up

# These times can be represented by the following list:
# [0, 5, 25, 30, 55]

# And now we can use a . character represents a minute spent awake
# And now we can use a # character represents a minute spent asleep

# So we could represent the data above by a string in the following way:
# ".....####################.....#########################....."

# Implement a function that will take an list of time intervals for being
#  awake/asleep over 60 mins and will generate a string encoding this
#  information with a series of . and #


def encode_times(times):
    pass


def test_encode_times_can_encode_a_series_of_times_into_a_time_string():
    assert encode_times(
        [0, 5, 25, 30, 55]) == (
            ".....####################.....#########################.....")
    assert encode_times(
        [0, 40, 50]) == (
            "........................................##########..........")
    assert encode_times(
        [0, 24, 29]) == (
            "........................#####...............................")

    # feel free to create your own assertions too with this challenge
