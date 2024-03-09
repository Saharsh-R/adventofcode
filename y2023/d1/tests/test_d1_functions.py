import pytest
from ..d1 import parse_value_from_string

@pytest.mark.parametrize(
    "input_string, expected_digit",
    [
        ("1sfgswf", 11),
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ],
)
def test_parse_value_from_string(input_string, expected_digit):
    """
    making sure parse function works as expected
    """
    assert parse_value_from_string(input_string) == expected_digit
    # assert parse_value_from_string(input_string) == expected_number
