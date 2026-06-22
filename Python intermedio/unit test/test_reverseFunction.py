from reverseFunction import reverse_string


def test_reverse_string_valid_input():
    # Arrange
    input_string = "Juan"
    # Act
    result = reverse_string(input_string)
    # Assert
    expected_output = "nauJ"
    assert result == expected_output


def test_reverse_string_valid_input_sentence():
    # Arrange
    input_string = "Hello World"
    # Act
    result = reverse_string(input_string)
    # Assert
    expected_output = "dlroW olleH"
    assert result == expected_output


def test_reverse_string_valid_input_number_and_letters():
    # Arrange
    input_string = "Juan123"
    # Act
    result = reverse_string(input_string)
    # Assert
    expected_output = "321nauJ"
    assert result == expected_output
