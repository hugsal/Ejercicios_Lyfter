import random
import pytest
from bubbleSortUnit import bubble_sort


def test_bubble_sort_with_small_list():
    # Arrange
    input_list = [5, 3, 1, 4]
    # Act
    result = bubble_sort(input_list)
    # Assert
    assert result == [1, 3, 4, 5]


def test_bubble_sort_with_big_list():
    # Arrange
    random_list = list(range(1, 102))
    random.shuffle(random_list)
    # Act
    result = bubble_sort(random_list)
    # Assert
    ordered_list = sorted(random_list)
    assert result == ordered_list


def test_bubble_sort_with_empty_list():
    # Arrange
    input_list = []
    # Act
    result = bubble_sort(input_list)
    # Assert
    assert result == []


def test_get_an_exception_with_a_value_not_valid():
    # Arrange
    input_list = [1, 2, "a", 4]
    # Act
    with pytest.raises(ValueError):
        bubble_sort(input_list)
