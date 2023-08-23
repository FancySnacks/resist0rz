"""Manager class for calculating total resistance on a color-coded single resistor"""

from abc import ABC, abstractmethod

from resist0rz.ColorBand import ColorBand
from resist0rz.const import COLOR_VALUES, InvalidColorName, Unit, UNITS
from resist0rz.util import is_a_color_name, is_smd_decimal_value, convert_unit


class Calculator(ABC):
    """Base abstract class for resistance calculation"""
    @abstractmethod
    def add_value(self, value):
        """Add single symbol or color marked on surface of resistor"""
        pass
    
    @abstractmethod
    def get_base_resistance_value(self) -> int:
        """Get base resistance value of resistor, without multiplying"""
        pass

    @abstractmethod
    def get_resistance_values(self, unit: str = "ohm") -> dict:
        """Get resistance values of resistor mapped to a dictionary"""
        pass

    def _get_desired_unit_name(self, unit: str) -> str:
        if unit.lower() in UNITS:
            return f"{unit}Ohm"
        else:
            return "Ohm"


class ColorBandCalculator(Calculator):
    """Calculate resistance value of a color-coded carbon resistor"""
    def __init__(self):
        self.values: list[ColorBand] = []
        self._values_original: list[ColorBand] = []
        self._multiplier_color: ColorBand | None = None
        self._tolerance_color: ColorBand | None = None

    @property
    def multiplier_color(self) -> ColorBand:
        return self._multiplier_color

    @multiplier_color.setter
    def multiplier_color(self, color: str):
        if not is_a_color_name(color):
            raise InvalidColorName(f"{color} is not a valid color name!")

        color_data: dict = COLOR_VALUES[color.upper()]
        self._multiplier_color = ColorBand(**color_data)

    @property
    def tolerance_color(self) -> ColorBand:
        return self._tolerance_color

    @tolerance_color.setter
    def tolerance_color(self, color: str):
        if not is_a_color_name(color):
            raise InvalidColorName(f"{color} is not a valid color name!")

        color_data: dict = COLOR_VALUES[color.upper()]

        if color_data['TOLERANCE'] != "None":
            self._tolerance_color = ColorBand(**color_data)
        else:
            raise ValueError("This color has no tolerance value")

    def _add_tolerance_and_multiplier_from_value_list(self):
        """If multiplier color/tolerance color is not set, choose one from value_colors property"""
        if not self.multiplier_color:
            self.multiplier_color = str(self.values.pop(-2))

        if not self.tolerance_color:
            self.tolerance_color = str(self.values.pop(-1))

    def add_value(self, color: str):
        if not is_a_color_name(color):
            raise InvalidColorName(f"{color} is not a valid color name!")

        color_data: dict = COLOR_VALUES[color.upper()]
        color_to_add: ColorBand = ColorBand(**color_data)
        self.values.append(color_to_add)
        self._values_original.append(color_to_add)

    def get_base_resistance_value(self) -> int:
        """Calculate resistance value without applying multiplier or tolerance"""
        total_resistance: list[str] = [str(color.VALUE) for color
                                       in self.values
                                       if color.VALUE != "None"]

        total_resistance: str = "".join(total_resistance)
        return int(total_resistance)

    def get_multiplied_resistance_value(self, base_value: int) -> int:
        """Apply multiplier to already calculated base resistance value"""
        if self.multiplier_color:
            return int(base_value * self.multiplier_color.MULTIPLIER)

        return base_value

    def get_tolerance_range(self, base_value: int) -> tuple[float, float]:
        min_resistance = base_value * (1 - self.tolerance_color.TOLERANCE)
        max_resistance = base_value * (1 + self.tolerance_color.TOLERANCE)

        return min_resistance, max_resistance

    def get_resistance_values(self, unit: str = "ohm") -> dict:
        """Calculate base, multiplied base and tolerance range and map values into a dictionary"""

        self._add_tolerance_and_multiplier_from_value_list()

        base = self.get_base_resistance_value()
        multiplied_base = self.get_multiplied_resistance_value(base)
        tolerance_range = self.get_tolerance_range(multiplied_base)

        if unit != "ohm":
            multiplied_base = convert_unit(unit=Unit[unit.upper()], value=str(multiplied_base))
            tolerance_range = (convert_unit(unit=Unit[unit.upper()], value=str(tolerance_range[0])),
                               convert_unit(unit=Unit[unit.upper()], value=str(tolerance_range[1])))

        result = {
            "values": self._values_original,
            "resistance": multiplied_base + f" {self._get_desired_unit_name(unit)}",
            "tolerance_range": self._tolerance_range_format(tolerance_range) + f" {self._get_desired_unit_name(unit)}"
        }

        return result

    def _tolerance_range_format(self, tolerance_range: tuple) -> str:
        return f"{tolerance_range[0]} - {tolerance_range[1]}"


class SMDCalculator(Calculator):
    """Calculates resistance values of SMD-type resistors"""
    def __init__(self):
        self.values: list[str] = []

    def add_value(self, value: str):
        self.values.append(value)

    def get_base_resistance_value(self) -> float:
        if is_smd_decimal_value("".join(self.values)):
            return self._get_decimal_resistance_value()
        else:
            return self._get_multiplied_resistance_value()

    def _get_decimal_resistance_value(self) -> float:
        result = ""

        for v in self.values:
            if v.lower() == "r":
                result += "."
            else:
                result += v

        return float(result)

    def _get_multiplied_resistance_value(self) -> int:
        multiplier = int(self.values[-1])
        base = int("".join(self.values[:-1:]))

        if multiplier > 0:
            return int(str(base) + str(multiplier * "0"))
        else:
            return int("".join(self.values))

    def get_resistance_values(self, unit: str = "ohm") -> dict:
        return {
            "value": ("".join(self.values), False),
            "resistance": (self.get_base_resistance_value(), True)
        }
