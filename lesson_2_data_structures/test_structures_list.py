import random
import pytest


@pytest.fixture
def create_list():
    """
    :return: list with random len between 5 to 15 with random numbers in range 0 to 10
    """
    return [random.randrange(0, 10) for i in range(random.randrange(5, 15))]


@pytest.mark.parametrize("new_element", [
    5,
    0,
    "one",
    r'!}#@?/\%',
    ""
])
def test_append(create_list, new_element):
    """
    Testing append list method
    """
    old_len = len(create_list)

    create_list.append(new_element)

    assert (old_len + 1) == len(create_list)
    assert new_element == create_list[-1]


def test_pop(create_list):
    """
    Testing pop list method
    """
    old_len = len(create_list)
    value = create_list[3]

    pop_value = create_list.pop(3)

    assert (old_len - 1) == len(create_list)
    assert value == pop_value


def test_reverse(create_list):
    """
    Testing reverse list method
    """
    new_list = create_list[:]
    new_list.reverse()

    assert create_list[0] == new_list[-1]
    assert create_list[-1] == new_list[0]
    assert create_list[::-1] == new_list


def test_sort(create_list):
    """
    Testing sort list method
    """
    new_list = create_list[:]
    new_list.sort(reverse=True)
    create_list.sort()

    assert new_list[::-1] == create_list


def test_copy(create_list):
    """
    Testing copy list method
    """
    new_list = create_list[:]
    copy_list = create_list.copy()

    assert create_list == new_list == copy_list
