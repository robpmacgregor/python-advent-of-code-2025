import pytest

from src.day_two.functions import inclusive_range_from_string, validate_id


def test_inclusive_range_from_string_returns_list_of_ids_from_range():
    r_str = '1-30'

    r_list = inclusive_range_from_string(r_str)

    assert r_list == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]


def test_validate_id_returns_true_for_valid_id():
    id = 123
    assert validate_id(id) is True

def test_validate_id_returns_false_for_invalid_id():
    id = 1313
    assert validate_id(id) is False

@pytest.mark.parametrize("test_input", [111, 1313, 145145145, 676767, 88])
def test_validate_id_regex_returns_false_for_invalid_id(test_input):
    assert validate_id(test_input) is False

@pytest.mark.parametrize("test_input", [1, 121, 13132, 1045145145, 67618767, 808])
def test_validate_id_regex_returns_true_for_valid_id(test_input):
    assert validate_id(test_input) is True