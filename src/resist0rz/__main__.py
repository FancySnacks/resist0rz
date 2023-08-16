"""Entry point for the script"""

from typing import Optional, Sequence

from .App import App
from .Parser import ArgParser
from .ColorCalculator import ColorBandCalculator, Calculator


def set_calculator_in_use(calc_type: str) -> Calculator:
    match calc_type:
        case 'color': return ColorBandCalculator()
        case 'smd': return ColorBandCalculator()
        case default: raise Exception("Invalid resistor type")


def main(argv: Optional[Sequence[str]] = None):
    parser = ArgParser(argv)
    parsed_args = parser.parse_args()

    calculator = set_calculator_in_use(parsed_args['type'])
    app = App(calculator)

    resistor_value: list[str] = parser.parse_colors(parsed_args['value'])

    result: dict = app.calculate_resistance(resistor_value)
    app.print_resistance_value(*result.values())


if __name__ == '__main__':
    main()
