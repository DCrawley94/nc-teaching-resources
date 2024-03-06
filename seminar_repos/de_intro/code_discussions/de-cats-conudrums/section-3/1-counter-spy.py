import pytest

# This function takes an list of names.
# The function should return an list containing the names of the people who
#  aren't spies.
# Recent intelligence has revealed that all spies codenames include the
#  letters 's', 'p' or 'y'.
# You can't afford to take any chances, and all names that include those
#  letters should be removed.


def counter_spy(people):
    pass


def test_counter_spy_returns_an_empty_list_if_the_only_person_is_a_spy():
    assert counter_spy(['Simon']) == []


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_counter_spy_returns_a_list_with_all_spies_removed():
    assert counter_spy(['Simon', 'Cat', 'Kyle']) == ['Cat']
    assert counter_spy(['Simon', 'Cat', 'Kyle', 'Danika', 'Alex', 'Chon']) == [
        'Cat', 'Danika', 'Alex', 'Chon']


# EXTRA CREDIT:

# Also, our spy admin team have asked that the names come back in alphabetical
#  order, for spy filing purposes.
# So if you could do that you'd really be saving them a lot of work. Thanks.

@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_counter_spy_returns_a_list_with_names_in_alphabetical_order():
    assert counter_spy(['Simon', 'Cat', 'Kyle', 'Danika', 'Alex', 'Chon']) == [
        'Alex', 'Cat', 'Chon', 'Danika']
