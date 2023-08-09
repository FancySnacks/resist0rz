"""Helper functions"""

import json


def load_color_values() -> list[dict]:
    """Load possible colors and their values as list of dicts"""
    with open("./colors_default.json", "r") as f:
        colors = json.load(f)
    return colors['colors']


def create_color_list(colors: list[dict]) -> dict:
    """Map a list of colors as dicts to a single dict"""
    return {color['NAME']: color for color in colors}
