import pytest

from resist0rz.ColorCalculator import ColorBandCalculator
from resist0rz.const import Color


@pytest.mark.parametrize("colors, expected_value", [
    ([Color.ORANGE, Color.ORANGE, Color.BLACK], 330),
    ([Color.BROWN, Color.BLACK], 10),
    ([Color.BROWN, Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN], 12345),
])
def test_calculate_base_value(colors, expected_value):
    calculator = ColorBandCalculator()

    for color in colors:
        calculator.add_color(color)

    assert calculator.get_base_resistance_value() == expected_value


@pytest.mark.parametrize("colors, multiplier, expected_value", [
    ([Color.ORANGE, Color.ORANGE, Color.BLACK], Color.BLACK, 330),
    ([Color.BROWN, Color.BLACK], Color.RED, 1000),
    ([Color.GREEN, Color.RED, Color.GREEN], Color.BROWN, 5250),
])
def test_calculate_multiplied_value(colors, multiplier, expected_value):
    calculator = ColorBandCalculator()

    for color in colors:
        calculator.add_color(color)

    calculator.multiplier_color = multiplier
    base_value = calculator.get_base_resistance_value()

    assert calculator.apply_multiplier(base_value) == expected_value

