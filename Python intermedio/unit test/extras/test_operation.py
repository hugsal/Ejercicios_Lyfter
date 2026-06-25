from operations import Operations

# Positive numbers
operation1 = Operations(10, 20)


def test_positive_numbers_add():
    # Act
    actual_result = operation1.add()
    # Assert
    expected_result = 30
    assert actual_result == expected_result


def test_positive_numbers_average():
    # Act
    actual_result = operation1.average()
    # Assert
    expected_result = 15.0
    assert actual_result == expected_result


def test_positive_numbers_multiply():
    # Act
    actual_result = operation1.multiply()
    # Assert
    expected_result = 200
    assert actual_result == expected_result


# Negative numbers
operation2 = Operations(-10, -20)


def test_negative_numbers_add():
    # Act
    actual_result = operation2.add()
    # Assert
    expected_result = -30
    assert actual_result == expected_result


def test_negative_numbers_average():
    # Act
    actual_result = operation2.average()
    # Assert
    expected_result = -15.0
    assert actual_result == expected_result


def test_negative_numbers_multiply():
    # Act
    actual_result = operation2.multiply()
    # Assert
    expected_result = 200
    assert actual_result == expected_result


# Cero cases
operation3 = Operations(15, 0)


def test_cero_cases_add():
    # Act
    actual_result = operation3.add()
    # Assert
    expected_result = 15
    assert actual_result == expected_result


def test_cero_cases_average():
    # Act
    actual_result = operation3.average()
    # Assert
    expected_result = 7.5
    assert actual_result == expected_result


def test_cero_cases_multiply():
    # Act
    actual_result = operation3.multiply()
    # Assert
    expected_result = 0
    assert actual_result == expected_result
