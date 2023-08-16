"""Manager class for calculating total resistance on a color-coded single resistor"""

from abc import ABC, abstractmethod

from .ColorBand import ColorBand
from .const import COLOR_VALUES
from .util import is_a_color_name


class Calculator(ABC):
    @abstractmethod
    def add_value(self, value):
        pass
    
    @abstractmethod
    def get_base_resistance_value(self) -> int:
        pass
    
    @abstractmethod
    def apply_multiplier(self, base_value: int) -> int:
        pass

    @abstractmethod
    def get_resistance_values(self):
        pass


class ColorBandCalculator(Calculator):
    def __init__(self):
        self.value_colors: list[ColorBand] = []
        self._multiplier_color: ColorBand | None = None
        self._tolerance_color: ColorBand | None = None

    @property
    def multiplier_color(self) -> ColorBand:
        return self._multiplier_color

    @multiplier_color.setter
    def multiplier_color(self, color: str):
        if not is_a_color_name(color):
            raise ValueError(f"{color} is not a valid color name!")

        color_data: dict = COLOR_VALUES[color.upper()]
        self._multiplier_color = ColorBand(**color_data)

    @property
    def tolerance_color(self) -> ColorBand:
        return self._tolerance_color

    @tolerance_color.setter
    def tolerance_color(self, color: str):
        if not is_a_color_name(color):
            raise ValueError(f"{color} is not a valid color name!")

        color_data: dict = COLOR_VALUES[color.upper()]

        if color_data['TOLERANCE'] != "None":
            self._tolerance_color = ColorBand(**color_data)
        else:
            raise ValueError("This color has no tolerance value")

    def _add_tolerance_and_multiplier_from_value_list(self):
        """If multiplier color/tolerance color is not set, choose one from value_colors property"""
        if not self.multiplier_color:
            self.multiplier_color = str(self.value_colors.pop(-2))

        if not self.tolerance_color:
            self.tolerance_color = str(self.value_colors.pop(-1))

    def add_value(self, color: str):
        if not is_a_color_name(color):
            raise ValueError(f"{color} is not a valid color name!")

        color_data: dict = COLOR_VALUES[color.upper()]
        color_to_add: ColorBand = ColorBand(**color_data)
        self.value_colors.append(color_to_add)

    def get_base_resistance_value(self) -> int:
        """Calculate resistance value without applying multiplier or tolerance"""
        total_resistance: list[str] = [str(color.VALUE) for color
                                       in self.value_colors
                                       if color.VALUE != "None"]

        total_resistance: str = "".join(total_resistance)
        return int(total_resistance)

    def apply_multiplier(self, base_value: int) -> int:
        """Apply multiplier to already calculated base resistance value"""
        if self.multiplier_color:
            return int(base_value * self.multiplier_color.MULTIPLIER)

        return base_value

    def get_tolerance_range(self, base_value: int) -> tuple[float, float]:
        min_resistance = base_value * (1 - self.tolerance_color.TOLERANCE)
        max_resistance = base_value * (1 + self.tolerance_color.TOLERANCE)

        return min_resistance, max_resistance

    def get_resistance_values(self) -> dict[str: int|float]:
        """Calculate base, multiplied base and tolerance range and map values into a dictionary"""

        self._add_tolerance_and_multiplier_from_value_list()

        base = self.get_base_resistance_value()
        multiplied_base = self.apply_multiplier(base)
        tolerance_range = self.get_tolerance_range(multiplied_base)

        result = {"base": base,
                  "multiplied": multiplied_base,
                  "tolerance_range": tolerance_range}

        return result
