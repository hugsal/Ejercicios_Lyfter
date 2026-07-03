from primos import get_primo_numbers


def test_get_primo_numbers():
    # Arrange
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Act
    result = get_primo_numbers(input_list)
    # Assert
    expected_list = [2, 3, 5, 7]
    assert result == expected_list


def test_get_primo_numbers_with_empty_list():
    # Arrange
    input_list = []
    # Act
    result = get_primo_numbers(input_list)
    # Assert
    assert result == []


def test_get_unique_primo_number():
    # Arrange
    input_list = [4, 6, 8, 10, 11, 12, 13]
    # Act
    result = get_primo_numbers(input_list)
    # Assert
    expected_list = [11]
