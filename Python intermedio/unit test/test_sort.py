from sort import get_list_from_string, get_string_from_list


def test_get_list_from_string_valid_input():
    # Arrange
    input_string = "python-variable-funcion-computadora-monitor"
    # Act
    result = get_list_from_string(input_string)
    # Assert
    expected_output = ["python", "variable", "funcion", "computadora", "monitor"]
    assert result == expected_output


def test_get_string_from_list_valid_input():
    # Arrange
    input_list = ["python", "variable", "funcion", "computadora", "monitor"]
    # Act
    result = get_string_from_list(input_list)
    # Assert
    expected_output = "python-variable-funcion-computadora-monitor"
    assert result == expected_output


def test_sort_valid_input():
    # Arrange
    input_list = ["python", "variable", "funcion", "computadora", "monitor"]
    # Act
    result = sorted(input_list)
    # Assert
    expected_output = ["computadora", "funcion", "monitor", "python", "variable"]
    assert result == expected_output
