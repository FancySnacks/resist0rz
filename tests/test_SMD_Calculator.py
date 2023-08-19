import pytest

from resist0rz.Calculator import SMDCalculator


@pytest.mark.parametrize("value, expected", [
    ("6R8", 6.8),
    ("R55", 0.55),
    ("12R53", 12.53)
])
def test_calculate_resistance_with_decimal_point(value, expected):
    calculator = SMDCalculator()

    for v in value:
        calculator.add_value(v)

    result = calculator.get_resistance_values()

    assert result['resistance'][0] == expected


@pytest.mark.parametrize("value, expected", [
    ("312", 3100.0)
])
def test_calculate_regular_SMD_value(value, expected):
    calculator = SMDCalculator()

    for v in value:
        calculator.add_value(v)

    result = calculator.get_resistance_values()

    assert result['resistance'][0] == expected
