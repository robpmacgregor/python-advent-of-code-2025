import pytest
from src.day_one.safe import Safe


def test_rotate_dial_returns_current_position_after_right_rotation():
    safe = Safe()

    assert safe.rotate_dial("R50") == (50, 0)
    assert safe.rotate_dial("R50") == (0, 1)

def test_rotate_dial_returns_current_position_after_left_rotation():
    safe = Safe()

    assert safe.rotate_dial("L50") == (50, 0)
    assert safe.rotate_dial("L50") == (0, 1)

def test_rotate_dial_returns_current_position_when_start_position_is_set():
    safe = Safe(20)

    assert safe.rotate_dial("L50") == (70, 1)
    assert safe.rotate_dial("L50") == (20, 0)

def test_rotate_dial_with_bad_prefix_raises_value_error():
    safe = Safe()

    with pytest.raises(ValueError) as e:
        safe.rotate_dial("H0")

def test_rotate_dial_returns_current_position_after_multiple_right_rotations():
    safe = Safe()

    assert safe.rotate_dial("R847") == (47, 8)

def test_rotate_dial_returns_current_position_after_multiple_left_rotations():
    safe = Safe()

    assert safe.rotate_dial("L847") == (53, 8)

def test_rotate_dial_returns_position_and_number_of_rotations():
    safe = Safe(50)

    assert safe.rotate_dial("R200") == (50, 2)
    assert safe.rotate_dial("R251") == (1, 3)