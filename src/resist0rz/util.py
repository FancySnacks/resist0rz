"""Various utility functions"""

from resist0rz.const import COLOR_NAMES


def is_a_color_name(color_name: str) -> bool:
    return color_name.upper() in COLOR_NAMES


def split_colors(color_str: str) -> list[str]:
    return color_str.replace(" ", "").split(",")


def parse_colors(color_str: str) -> list[str]:
    """Parse a string of comma separated color names into a list of strings"""
    if is_valid_resistance_value(color_str):
        return split_colors(color_str)


def parse_raw_value(value: str) -> list[str]:
    """Parse SMD resistor value into a list of strings"""
    if is_valid_resistance_value(value):
        return list(value)


def is_valid_resistance_value(value: list[str] | str) -> bool:
    """Check if passed list of color bands / SMD value list has minimum length of 3 values"""
    if len(value) < 3:
        raise Exception("Resistor value has to have a minimum length of 3!")
    return True


def is_smd_decimal_value(smd_value: str) -> bool:
    """Search for 'R' divider in a smd resistor value"""
    return True if smd_value.lower().find("r") > -1 else False


# TODO: Check whether the input value is mismatched, ex. user is trying to pass SMD encoded value while the resistor
# type specified is of color type (or vice versa)
