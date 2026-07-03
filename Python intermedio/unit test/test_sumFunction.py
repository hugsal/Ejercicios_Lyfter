from sumFunction import sum_list_elements


def test_sum_list_elements_valid_input():
    # Arrange
    input_list = [1, 2, 3, 4, 5]
    # Act
    result = sum_list_elements(input_list)
    # Assert
    expected_output = 15
    assert result == expected_output


def test_sum_list_elements_valid_input_negatives():
    # Arrange
    input_list = [-1, -2, -3, -4, -5]
    # Act
    result = sum_list_elements(input_list)
    # Assert
    expected_output = -15
    assert result == expected_output


def test_sum_list_elements_valid_input_float():
    # Arrange
    input_list = [1.1, 2.2, 3.3, 4.4, 5.5]
    # Act
    result = sum_list_elements(input_list)
    # Assert
    expected_output = 16.5
    assert result == expected_output
