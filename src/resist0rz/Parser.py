from argparse import ArgumentParser, RawTextHelpFormatter
from typing import Sequence


class ArgParser:
    def __init__(self, args: Sequence[str]):
        """
            ArgumentParser class for parsing console args.

            usage: resc [args]

            Get the resistance value of any color-coded or SMD resistor

            options:
              -h, --help            show this help message and exit
              -t RESISTOR_TYPE, --type RESISTOR_TYPE
                                    Type of measured resistor.
                                    Depending on the type specified a different way of calculation is used.
                                    Options: ['color' (default) | 'smd']
              -v RESISTOR_VALUE, --value RESISTOR_VALUE
                                    Value of a given resistor, matching the chosen type.
                                    'color' - string sequence of full color names (ex. 'brown,black,black').
                                    Color names have to be separated by commas
                                    Minimum of 3 colors for value to be calculated. (base + multiplier + tolerance)
                                    'smd' - string value of a SMD type resistor. The value has to input the way it appears on the resistor's surface
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
                                  required=True)

    def parse_colors(self, color_str: str) -> list[str]:
        color_list: list[str] = color_str.replace(" ", "").split(",")

        if self._minimum_color_count_met(color_list):
            return color_list
        else:
            raise Exception("Requirement of minimum 3 colors has to be met!")


    def _minimum_color_count_met(self, colors: list[str]) -> bool:
        if len(colors) < 3:
            return False
        return True
