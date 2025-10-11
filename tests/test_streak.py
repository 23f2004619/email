import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Tests that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Tests that the function returns the length of the longest streak."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_zeros_and_negatives():
    """Tests that the function handles zeros and negative numbers correctly."""
    assert longest_positive_streak([-1, -2, 0, -3]) == 0
    assert longest_positive_streak([1, 2, 0, 3, 4, 5, -1, 6]) == 3
