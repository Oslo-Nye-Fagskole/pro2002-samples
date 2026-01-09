# test_calculator.py

from calculator import add_numbers

# Test names should read like sentences and describe the expected behavior.
# This makes it clear what the code under test is supposed to do.
def test_add_numbers_returns_sum_of_two_values():
    # Arrange
    a = 2
    b = 3

    # Act
    result = add_numbers(a, b)

    # Assert
    assert result == 5