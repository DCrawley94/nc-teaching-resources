from test_api.checks import run_test, skip_test, format_err_msg

# This function takes a list of names.
# The function should return a list containing the names of the people who
#  aren't spies.
# Recent intelligence has revealed that all spies codenames include the
#  letters 's', 'p' or 'y'.
# You can't afford to take any chances, and all names that include those
#  letters should be removed.


def counter_spy(people):
    pass


@run_test
def test_counter_spy_returns_an_empty_list_if_the_only_person_is_a_spy():
    assert counter_spy(['Simon']) == [], format_err_msg(
        [], counter_spy(['Simon']))


@skip_test
def test_counter_spy_returns_a_list_with_all_spies_removed():
    assert counter_spy(['Simon', 'Cat', 'Kyle']) == ['Cat'], \
        format_err_msg(['Cat'], counter_spy(['Simon', 'Cat', 'Kyle']))
    assert counter_spy(['Simon', 'Alex', 'Kyle', 'Cat', 'Chon', 'Danika']) == [
        'Alex', 'Cat', 'Chon', 'Danika'], \
        format_err_msg(['Alex', 'Cat', 'Chon', 'Danika'], counter_spy(
            ['Simon', 'Alex', 'Kyle', 'Cat', 'Chon', 'Danika']))


# EXTRA CREDIT:

# Also, our spy admin team have asked that the names come back in alphabetical
#  order, for spy filing purposes.
# So if you could do that you'd really be saving them a lot of work. Thanks.

@skip_test
def test_counter_spy_returns_a_list_with_names_in_alphabetical_order():
    assert counter_spy(['Simon', 'Cat', 'Kyle', 'Danika', 'Alex', 'Chon']) == [
        'Alex', 'Cat', 'Chon', 'Danika'], \
        format_err_msg(['Alex', 'Cat', 'Chon', 'Danika'], counter_spy(
            ['Simon', 'Cat', 'Kyle', 'Danika', 'Alex', 'Chon']))


if __name__ == "__main__":
    test_counter_spy_returns_an_empty_list_if_the_only_person_is_a_spy()
    test_counter_spy_returns_a_list_with_all_spies_removed()
    test_counter_spy_returns_a_list_with_names_in_alphabetical_order()
