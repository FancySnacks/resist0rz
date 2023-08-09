"""Manager class for calculating total resistance on a color-coded single resistor"""

from .ColorBand import ColorBand
from .const import COLOR_VALUES, Color


class ColorBandCalculator:
    def __init__(self):
        self.value_colors: list[ColorBand] = []
        self._multiplier_color: ColorBand | None = None
        self.tolerance_color: ColorBand | None = None

    @property
    def multiplier_color(self) -> ColorBand:
        return self._multiplier_color

    @multiplier_color.setter
    def multiplier_color(self, color: Color):
        color_data: dict = COLOR_VALUES[color.upper()]
        self._multiplier_color = ColorBand(**color_data)

    def add_color(self, color: Color):
        color_data: dict = COLOR_VALUES[color.upper()]
        color_to_add: ColorBand = ColorBand(**color_data)
        self.value_colors.append(color_to_add)

    def get_base_resistance_value(self) -> int:
        """Calculate resistance value without applying multiplier or tolerance"""
        total_resistance: list[str] = [str(color.VALUE) for color
                                       in self.value_colors
                                       if color.VALUE is not None]

        total_resistance: str = "".join(total_resistance)
        return int(total_resistance)

    def apply_multiplier(self, base_value: int) -> int:
        """Apply multiplier to already calculated base resistance value"""
        if self.multiplier_color:
            return int(base_value * self.multiplier_color.MULTIPLIER)

        return base_value

    def get_tolerance_range(self):
        pass
