import pytest

from src.day_three.functions import find_highest_digits_in_order

@pytest.mark.parametrize("seq, expected", [('4579047780346634', 98), ('4578047780346639', 89)])
def test_find_highest_digits_in_order(seq, expected):
    actual = find_highest_digits_in_order(seq, 2)

    assert actual == expected
