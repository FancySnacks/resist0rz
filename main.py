import json
from dataclasses import dataclass
from enum import StrEnum, Enum, auto


def load_color_values() -> list:
    with open("./colors_default.json", "r") as f:
        colors = json.load(f)
    return colors['colors']


def create_color_definitions(colors: list[dict]) -> dict:
    return {color['NAME']: color for color in colors}


COLOR_VALUES: dict = create_color_definitions(load_color_values())


class Unit(Enum):
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


@dataclass(frozen=True)
class ColorBand:
    NAME: str
    VALUE: int | None
    MULTIPLIER: float
    TOLERANCE: float | None

    def __repr__(self) -> str:
        return self.NAME


class ColorBandCalculator:
    def __init__(self):
        self.value_colors: list[ColorBand] = []
        self._multiplier_color: ColorBand | None = ...
        self.tolerance_color: ColorBand | None = ...

    @property
    def multiplier_color(self) -> ColorBand:
        return self._multiplier_color

    @multiplier_color.setter
    def multiplier_color(self, color: Color):
        color_data: dict = COLOR_VALUES[color.upper()]
        if color_data['MULTIPLIER'] is not None:
            self._multiplier_color = ColorBand(**color_data)

    def add_color(self, color: Color):
        color_data: dict = COLOR_VALUES[color.upper()]
        color_to_add: ColorBand = ColorBand(**color_data)
        self.value_colors.append(color_to_add)

    def get_base_resistance_value(self) -> int:
        total_resistance: list[str] = [str(color.VALUE) for color
                                       in self.value_colors
                                       if color.VALUE is not None]

        total_resistance: str = "".join(total_resistance)
        return int(total_resistance)

    def apply_multiplier(self, base_value: int) -> int:
        if self.multiplier_color:
            return int(base_value * self.multiplier_color.MULTIPLIER)

        return base_value

    def get_tolerance_range(self):
        pass


a = ColorBandCalculator()
a.add_color(Color.RED)
a.add_color(Color.BLACK)
a.multiplier_color = Color.BROWN
print(a.value_colors)
base = a.get_base_resistance_value()
print(base)
multiplied = a.apply_multiplier(base)
print(multiplied)
