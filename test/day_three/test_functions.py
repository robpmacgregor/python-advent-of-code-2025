import pytest

from src.day_three.functions import find_highest_digits_in_order


@pytest.mark.parametrize("seq, expected, number_of_digits", [
    ('4579047780346634', 98, 2),
    ('4578047780346639', 89, 2),
    ('1222221321225242712221222525222223522222552272213272343272323223122224441115122732521232222222322222', 777775332222, 12),
    ('4232522222323233413342333432333223213412332114322331731312383343122233322123333223234314132322421423', 844433421423, 12),
])
def test_find_highest_digits_in_order(seq, expected, number_of_digits):
    actual = find_highest_digits_in_order(seq, number_of_digits)

    assert actual == expected
