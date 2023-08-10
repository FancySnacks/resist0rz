"""Entry point for the script"""

from typing import Optional, Sequence

from resist0rz.Parser import ArgParser
from resist0rz.ColorCalculator import ColorBandCalculator


def print_resistance(resistor_value, resistance: int, resistance_range: tuple[float, float]):
    print(f"VALUE: {resistor_value}")
    print(f"RESISTANCE: {resistance} Ohm")
    print(f"RANGE: {int(resistance_range[0])} Ohm - {int(resistance_range[1])} Ohm")


def main(argv: Optional[Sequence[str]] = None):
    parser = ArgParser()
    parsed_args: dict = parser.parse_args(argv)

    calculator = None
    total_resistance = ...

    if parsed_args['type'] == 'color':
        calculator = ColorBandCalculator()
        resistor_value: list[str] = parser.parse_colors(parsed_args['value'])

        calculator.multiplier_color = resistor_value.pop(-2)
        calculator.tolerance_color = resistor_value.pop(-1)

        for color in resistor_value:
            calculator.add_color(color)

        total_resistance: int = calculator.apply_multiplier(calculator.get_base_resistance_value())
        resistance_range: tuple[float, float] = calculator.get_tolerance_range(total_resistance)
    else:
        pass

    print_resistance(resistor_value, total_resistance, resistance_range)


if __name__ == '__main__':
    main()
