from .ColorCalculator import ColorBandCalculator
from .const import Color

if __name__ == '__main__':
    calculator = ColorBandCalculator()

    calculator.add_color(Color.ORANGE)
    calculator.add_color(Color.ORANGE)
    calculator.add_color(Color.BLACK)
    calculator.multiplier_color = Color.BLACK

    base_resistance = calculator.get_base_resistance_value()
    total_resistance = calculator.apply_multiplier(base_resistance)

    print(total_resistance)
