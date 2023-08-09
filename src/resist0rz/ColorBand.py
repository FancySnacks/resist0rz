"""Resistor color band data class"""

from dataclasses import dataclass, field


@dataclass(order=True)
class ColorBand:
    NAME: str
    VALUE: int | None
    MULTIPLIER: float
    TOLERANCE: float | None
    SORT_INDEX: int = field(init=False, repr=False)

    def __post_init__(self):
        self.SORT_INDEX = self.VALUE

    def __repr__(self) -> str:
        return self.NAME
