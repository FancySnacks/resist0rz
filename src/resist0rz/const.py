"""Various constant variables and definitions"""

import json
import pathlib

from enum import Enum, StrEnum, auto


DEFAULT_PATH = pathlib.Path(__file__).parent
COLORS_PATH = DEFAULT_PATH.joinpath(pathlib.Path("./colors_default.json"))


COLOR_TABLE = """
*-----------*-------------*-------------*---------------*---------------*
|   COLOR   |   Value 1   |   Value 2+  |   Multiplier  |   Tolerance   |
*-----------*-------------*-------------*---------------*---------------*
|   BLACK   |      0      |      0      |    x1         |               |
|   BROWN   |      1      |      1      |    x10        |     +- 1%     |
|    RED    |      2      |      2      |    x100       |     +- 2%     |
|   ORANGE  |      3      |      3      |    x1000      |               |
|   YELLOW  |      4      |      4      |    x10000     |               |
|   GREEN   |      5      |      5      |    x100000    |    +- 0.5%    |
|    BLUE   |      6      |      6      |    x1000000   |    +- 0.25%   |
|   VIOLET  |      7      |      7      |    x10000000  |    +- 0.10%   |
|    GREY   |      8      |      8      |               |    +- 0.05%   |
|   WHITE   |      9      |      9      |               |               |
|    GOLD   |             |             |    x0.1       |    +- 5%      |
|   SILVER  |             |             |    x0.01      |    +- 10%     |
*-----------------------------------------------------------------------*
"""


def load_color_values() -> list[dict]:
    """Load possible colors and their values as list of dicts"""
    with open(COLORS_PATH, "r") as f:
        colors = json.load(f)
    return colors['colors']


def create_color_list(colors: list[dict]) -> dict:
    """Map a list of colors as dicts to a single dict"""
    return {color['NAME']: color for color in colors}


COLORS: list[dict] = load_color_values()
COLOR_NAMES = [color['NAME'] for color in COLORS]
COLOR_VALUES: dict = create_color_list(COLORS)


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


UNITS = ["ohm"] + [e.name.lower() for e in Unit]


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


class InvalidColorName(Exception):
    """Raised when string supplied doesn't match any of existing resistor color bands"""
    def __init__(self, color_name: str, message="is not a valid color name!"):
        self.message = f"'{color_name}' {message}"
        super().__init__(self.message)
