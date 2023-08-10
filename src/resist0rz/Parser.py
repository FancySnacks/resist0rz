from argparse import ArgumentParser, RawTextHelpFormatter

from typing import Sequence


class ArgParser:
    def __init__(self):
        self._parser = ArgumentParser(prog="resist0rz",
                                      usage="resc [args]",
                                      description="Get the resistance value of any color-coded or SMD resistor",
                                      epilog="by FancySnacks @2023",
                                      formatter_class=RawTextHelpFormatter)
        self.args = None

        self._setup()

    def parse_args(self, args: Sequence[str]) -> dict:
        self.args = vars(self._parser.parse_args(args))
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
                                  type=str)
