import pytest
from divideNumbers import divide


def test_positive_numbers():
    # Arrange
    number1 = 10
    number2 = 2
    # Act
    actual_result = divide(number1, number2)
    # Assert
    expected_result = 5.0
    assert actual_result == expected_result


def test_cero_cases():
    # Arrange
    number1 = 10
    number2 = 0
    # Act
    with pytest.raises(ValueError):
        divide(number1, number2)


def test_string_cases():
    # Arrange
    number1 = 10
    number2 = "5"
    # Act
    with pytest.raises(TypeError):
        divide(number1, number2)
