from upperCase import get_total_upper_cases, get_total_lower_cases


def test_get_total_upper_cases_valid_input():
    # Arrange
    input_string = "Hello World"
    # Act
    result = get_total_upper_cases(input_string)
    # Assert
    expected_output = 2
    assert result == expected_output


def test_get_total_lower_cases_valid_input():
    # Arrange
    input_string = "Hello World"
    # Act
    result = get_total_lower_cases(input_string)
    # Assert
    expected_output = 8
    assert result == expected_output


def test_get_total_upper_cases_valid_input_sentence():
    # Arrange
    input_string = "My Name is Hugo SALAZAR"
    # Act
    result = get_total_upper_cases(input_string)
    # Assert
    expected_output = 10
    assert result == expected_output


def test_get_total_lower_cases_valid_input_sentence():
    # Arrange
    input_string = "My Name is Hugo SALAZAR"
    # Act
    result = get_total_lower_cases(input_string)
    # Assert
    expected_output = 9
    assert result == expected_output
