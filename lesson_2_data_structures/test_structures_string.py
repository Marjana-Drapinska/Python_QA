import pytest


@pytest.mark.parametrize("new_element", [
    'Some text',
    "one",
    r'!}#@?/\%',
    ""
])
def test_add(new_element):
    """
    Testing add string method
    """
    first_string = 'First string'

    concat_string = first_string + new_element

    assert len(first_string) + len(new_element) == len(concat_string)


def test_dubl():
    """
    Testing dubl string method
    """
    first_string = 'First string'

    new_string = first_string*3
    assert len(first_string)*3 == len(new_string)


def test_len():
    """
    Testing len string method
    """
    for i in range(1,10):
        string_1 = 'a' * i
        assert i == len(string_1)


def test_uppercase():
    """
    Testing upper string method
    """
    first_string = 'first string'

    first_string = first_string.upper()
    assert first_string.isupper()


def test_count():
    """
    Testing count string method
    """
    for i in range(1,10):
        string_1 = 'some tex' * i
        assert i == string_1.count('some tex')
