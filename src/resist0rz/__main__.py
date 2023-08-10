"""Entry point for the script"""

from typing import Optional, Sequence

from resist0rz.Parser import ArgParser
from resist0rz.ColorCalculator import ColorBandCalculator
from resist0rz.const import Color


def main(argv: Optional[Sequence[str]] = None):
    parser = ArgParser()
    parsed_args: dict = parser.parse_args(argv)

    calculator = ColorBandCalculator()

    calculator.add_color(Color.ORANGE)
    calculator.add_color(Color.ORANGE)
    calculator.add_color(Color.BLACK)
    calculator.multiplier_color = Color.BLACK

    base_resistance = calculator.get_base_resistance_value()
    total_resistance = calculator.apply_multiplier(base_resistance)

    print(total_resistance)


if __name__ == '__main__':
    main()
