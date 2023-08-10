"""Manager class for calculating total resistance on a color-coded single resistor"""

from resist0rz.ColorBand import ColorBand
from resist0rz.const import COLOR_VALUES, Color
from resist0rz.util import is_a_color_name_name


class ColorBandCalculator:
    def __init__(self):
        self.value_colors: list[ColorBand] = []
        self._multiplier_color: ColorBand | None = None
        self._tolerance_color: ColorBand | None = None

    @property
    def multiplier_color(self) -> ColorBand:
        return self._multiplier_color

    @multiplier_color.setter
    def multiplier_color(self, color: str):
        if not is_a_color_name_name(color):
            raise ValueError(f"{color} is not a valid color name!")

        color_data: dict = COLOR_VALUES[color.upper()]
        self._multiplier_color = ColorBand(**color_data)

    @property
    def tolerance_color(self) -> ColorBand:
        return self._tolerance_color

    @tolerance_color.setter
    def tolerance_color(self, color: str):
        if not is_a_color_name_name(color):
            raise ValueError(f"{color} is not a valid color name!")

        color_data: dict = COLOR_VALUES[color.upper()]

        if color_data['TOLERANCE'] != "None":
            self._tolerance_color = ColorBand(**color_data)
        else:
            raise ValueError("This color has no tolerance value")

    def add_color(self, color: str):
        if not is_a_color_name_name(color):
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
