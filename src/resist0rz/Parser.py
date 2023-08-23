from argparse import ArgumentParser, RawTextHelpFormatter
from typing import Sequence

from resist0rz.util import parse_raw_value, parse_colors


class ArgParser:
    def __init__(self, args: Sequence[str]):
        """
            usage: resc [args]

            Get the resistance value of any color-coded or SMD resistor

            options:
              -h, --help            show this help message and exit
              -t RESISTOR_TYPE, --type RESISTOR_TYPE
                                    Type of a measured resistor.
                                    Depending on the type specified a different way of calculation is used.
                                    Options: ['color' (default) | 'smd']
              -v RESISTOR_VALUE, --value RESISTOR_VALUE
                                    Value of a given resistor, matching the chosen type.
                                    'color' - string sequence of full color names (ex. 'brown,black,black').
                                    Color names have to be separated by commas
                                    Minimum of 3 colors for value to be calculated. (base + multiplier + tolerance)
                                    'smd' - string value of a SMD type resistor. The value has to inputted the way it appears on the resistor's surface
              -s, --simple          Print the results as dictionary instead of a formatted string.
              -c, --table           Print the color table to the console.
              -u CONVERSION_UNIT, --unit CONVERSION_UNIT
                                    Convert the result to a multiply of Ohms (micro, kilo, mega etc.)
                                    Enter the suffix of the unit you want, ex. enter 'kilo' instead of 'kiloohms' or other.
                                    example usage: resc -c 'orange,orange,black' -u 'mili' -> returns resisance in miliohms

            by FancySnacks @2023
        """
        self._parser = ArgumentParser(prog="resist0rz",
                                      usage="resc [args]",
                                      description="Get the resistance value of any color-coded or SMD resistor",
                                      epilog="by FancySnacks @2023",
                                      formatter_class=RawTextHelpFormatter)
        self.args = None

        self._setup()

    def parse_args(self) -> dict:
        self.args = vars(self._parser.parse_args())
        return self.args

    def _setup(self):
        self._parser.add_argument('-t',
                                  '--type',
                                  metavar='RESISTOR_TYPE',
                                  help="Type of a measured resistor.\n"
                                       "Depending on the type specified a different way of calculation is used.\n"
                                       "Options: ['color' (default) | 'smd']",
                                  choices=['color', 'smd'],
                                  default='color')

        self._parser.add_argument('-v',
                                  '--value',
                                  metavar='RESISTOR_VALUE',
                                  help="Value of a given resistor, matching the chosen type."
                                       "\n"
                                       "'color' - string sequence of full color names (ex. 'brown,black,black').\n"
                                       "Color names have to be separated by commas\n"
                                       "Minimum of 3 colors for value to be calculated. (base + multiplier + tolerance)"
                                       "\n"
                                       "'smd' - string value of a SMD type resistor. The value has to inputted the way "
                                       "it appears on the resistor's surface",
                                  type=str,
                                  required=False)

        self._parser.add_argument('-s',
                                  '--simple',
                                  help="Print the results as dictionary instead of a formatted string.",
                                  action="store_true")

        self._parser.add_argument('-c',
                                  '--table',
                                  action="store_true",
                                  help="Print the color table to the console.")

        self._parser.add_argument('-u',
                                  '--unit',
                                  type=str,
                                  metavar="CONVERSION_UNIT",
                                  help="Convert the result to a multiply of Ohms (micro, kilo, mega etc.)\n"
                                       "Enter the suffix of the unit you want, ex. enter 'kilo' instead of 'kiloohms' "
                                       "or other.\n"
                                       "example usage: resc -c 'orange,orange,black' -u 'mili' -> returns resisance in miliohms")

    def parse_resistor_value(self, value: str) -> list[str]:
        if self.args['type'] == 'color':
            return parse_colors(value)
        else:
            return parse_raw_value(value)
