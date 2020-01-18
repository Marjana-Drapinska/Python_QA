import random
import pytest


@pytest.fixture
def create_dict():
    """
    :return: dict with random len
    """
    return {a: a ** 2 for a in range(random.randrange(3, 10))}


def test_clear(create_dict):
    """
    Testing clear dict method
    """
    create_dict.clear()
    assert 0 == len(create_dict)


def test_pop(create_dict):
    """
    Testing pop dict method
    """
    old_len = len(create_dict)
    value = create_dict[2]

    pop_value = create_dict.pop(2)

    assert (old_len - 1) == len(create_dict)
    assert value == pop_value


def test_get(create_dict):
    """
    Testing get dict method
    """
    for i in range(0, len(create_dict)):
       assert i*i == create_dict.get(i)

@pytest.mark.parametrize('new_key, new_value', [
    ('A1', '1111'),
    (555, r'!}#@?/\%')
])
def test_update(create_dict, new_key, new_value):
    """
    Testing update dict method
    """
    old_len = len(create_dict)
    create_dict.update({new_key:new_value})

    assert (old_len + 1) == len(create_dict)
    assert new_value == create_dict[new_key]


def test_del(create_dict):
    """
    Testing del dict method
    """
    old_len = len(create_dict)
    del create_dict[1]

    assert (old_len - 1) == len(create_dict)
