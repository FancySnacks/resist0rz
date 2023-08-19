"""Entry point for the script"""

from typing import Optional, Sequence

from resist0rz.const import Unit
from resist0rz.util import convert_unit
from resist0rz.App import App
from resist0rz.Parser import ArgParser
from resist0rz.Calculator import ColorBandCalculator, SMDCalculator, Calculator


def set_calculator_in_use(calc_type: str) -> Calculator:
    match calc_type:
        case 'color': return ColorBandCalculator()
        case 'smd': return SMDCalculator()
        case default: raise Exception("Invalid resistor type")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = ArgParser(argv)
    parsed_args: dict = parser.parse_args()

    calculator_type: str = parsed_args['type']
    calculator = set_calculator_in_use(calculator_type)
    app = App(calculator)

    resistor_value = parser.parse_resistor_value(parsed_args['value'])

    result: dict = app.calculate_resistance(resistor_value)
    app.print_resistance_value(result)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
