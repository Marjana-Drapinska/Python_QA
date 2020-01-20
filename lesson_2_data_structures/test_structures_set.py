import pytest

@pytest.mark.parametrize('new_element', [
    5,  "one", r'!}#@?/\%', 2.0, (1, 2, 3)
])
def test_add(new_element):
    """ Testing add set method"""
    months = set(["Jan", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
    months.add(new_element)
    assert new_element in months


def test_discard():
    """ Testing discard set method """
    months = set(["Jan", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
    months.discard("Feb")
    assert not "Feb" in months


def test_clear():
    """ Testing clear set method """
    months = set(["Jan", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
    months.clear()
    assert 0 == len(months)


def test_copy():
    """ Testing copy set method """
    months = set(["Jan", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
    new_months = months.copy()
    assert months == new_months


def test_union():
    """ Testing union set method """
    months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
    months_b = set(["July", "Aug", "Sep", "Oct", "Nov", "Dec"])

    all_months = months_a.union(months_b)

    assert len(months_a) + len(months_b) == len(all_months)
    assert months_a.issubset(all_months)
    assert months_b.issubset(all_months)
