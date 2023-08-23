"""Main program functionality"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from resist0rz.Calculator import Calculator


class App:
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def _add_resistor_values(self, values: list):
        """Add list of resistor values (colors or numbers) for later calculation"""
        for item in values:
            self.calculator.add_value(item)

    def calculate_resistance(self, values: list, unit: str = "ohm"):
        """Calculates resistance value and returns a dict containing base, multiplied and tolerance range values"""
        self._add_resistor_values(values)
        values: dict = self.calculator.get_resistance_values(unit)

        return values

    def print_resistance_value(self, values: dict):
        """Print calculation results"""

        for v in values.items():
            buffer = f"{v[0].upper()}: {v[1]}"

            print(buffer)
