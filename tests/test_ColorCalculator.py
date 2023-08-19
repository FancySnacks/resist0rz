import pytest

from resist0rz.Calculator import ColorBandCalculator
from resist0rz.const import Color


@pytest.mark.parametrize("colors, expected_value", [
    ([Color.ORANGE, Color.ORANGE, Color.BLACK], 330),
    ([Color.BROWN, Color.BLACK], 10),
    ([Color.BROWN, Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN], 12345),
])
def test_calculate_base_value(colors, expected_value):
    calculator = ColorBandCalculator()

    for color in colors:
        calculator.add_value(color)

    assert calculator.get_base_resistance_value() == expected_value


@pytest.mark.parametrize("colors, expected_value", [
    ([Color.ORANGE, Color.ORANGE, Color.BLACK, Color.BLACK, Color.GOLD], 330),
    ([Color.BROWN, Color.BLACK, Color.RED, Color.GOLD], 1000),
    ([Color.GREEN, Color.RED, Color.GREEN, Color.BROWN, Color.SILVER], 5250),
])
def test_calculate_resistance_value(colors, expected_value):
    calculator = ColorBandCalculator()

    for color in colors:
        calculator.add_value(color)

    result = calculator.get_resistance_values()

    assert result['resistance'][0] == expected_value


def test_raises_exception_when_color_has_no_tolerance_value():
    with pytest.raises(ValueError):
        calculator = ColorBandCalculator()
        calculator.tolerance_color = Color.BLACK


@pytest.mark.parametrize("colors, multiplier, tolerance, expected_value", [
    ([Color.BROWN, Color.BLACK], Color.BROWN, Color.GOLD, "95.0 - 105.0"),
    ([Color.RED, Color.GREEN], Color.RED, Color.SILVER, "2250.0 - 2750.0"),
])
def test_tolerance_is_applied(colors, multiplier, tolerance, expected_value):
    calculator = ColorBandCalculator()

    for color in colors:
        calculator.add_value(color)

    calculator.multiplier_color = multiplier
    calculator.tolerance_color = tolerance

    result: dict = calculator.get_resistance_values()

    assert result['tolerance_range'][0] == expected_value
