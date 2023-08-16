from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Calculator import Calculator


class App:
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def _add_resistor_values(self, values: list):
        """Add list of resistor values (colors or numbers) for later calculation"""
        for item in values:
            self.calculator.add_value(item)

    def calculate_resistance(self, values: list):
        """Calculates resistance value and returns a dict containing base, multiplied and tolerance range values"""
        self._add_resistor_values(values)
        values: dict = self.calculator.get_resistance_values()

        return values

    def print_resistance_value(self, resistor_value, resistance: int, resistance_range: tuple[float, float]):
        print(f"VALUE: {resistor_value}")
        print(f"RESISTANCE: {resistance} Ohm")
        print(f"RANGE: {int(resistance_range[0])} Ohm - {int(resistance_range[1])} Ohm")
