"""Various constant variables and definitions"""

import pathlib

from enum import Enum, StrEnum, auto

from util import create_color_list, load_color_values


DEFAULT_PATH = pathlib.Path(__file__).parent

COLOR_VALUES: dict = create_color_list(load_color_values())


class Unit(Enum):
    """Represents singular Ohm conversion and its value as power"""
    PICO = -12
    NANO = -9
    MICRO = -6
    MILI = -3
    OHM = 1
    KILO = 3
    MEGA = 6
    GIGA = 9
    TERA = 12


class Color(StrEnum):
    """One of possible resistor color bands"""
    BLACK = auto()
    BROWN = auto()
    RED = auto()
    ORANGE = auto()
    YELLOW = auto()
    GREEN = auto()
    BLUE = auto()
    VIOLET = auto()
    GREY = auto()
    WHITE = auto()
    GOLD = auto()
    SILVER = auto()
