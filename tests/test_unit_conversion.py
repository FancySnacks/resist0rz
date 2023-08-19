import pytest

from resist0rz.util import convert_unit
from resist0rz.const import Unit


@pytest.mark.parametrize("value, unit, expected", [
    ("330", Unit.MILI, "330000"),
    ("1", Unit.MICRO, "1000000"),
    ("55", Unit.NANO, "55000000000"),
    ("3", Unit.PICO, "3000000000000")
])
def test_convert_to_smaller_unit(value, unit, expected):
    assert convert_unit(unit, value) == expected


@pytest.mark.parametrize("value, unit, expected", [
    ("330", Unit.KILO, "0.330"),
    ("33", Unit.KILO, "0.033"),
    ("3", Unit.KILO, "0.003"),
    ("1", Unit.MEGA, "0.00001"),
    ("55", Unit.GIGA, "0.00000055"),
    ("3", Unit.TERA, "0.00000000003"),
])
def test_convert_to_bigger_unit(value, unit, expected):
    assert convert_unit(unit, value) == expected
