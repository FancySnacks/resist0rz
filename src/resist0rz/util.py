from resist0rz.const import COLOR_NAMES


def is_a_color_name(color_name: str) -> bool:
    return color_name.upper() in COLOR_NAMES


def get_SMD_comma_index(value: str) -> int:
    return value.lower().find("r")
