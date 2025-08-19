from typing import List
from enum import StrEnum


class StackEnum(StrEnum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"


def volume_calc(width: float, height: float, length: float) -> float:
    return width * height * length

def has_bulky_dimension(dimensions: List[float]) -> bool:
    return any(d >= 150 for d in dimensions)

def has_heavy_mass(mass: float) -> bool:
    return mass >= 20

def check_inputs(values: List[float]):
    if any(v <= 0 for v in values):
        raise ValueError(f"All values must be greater than 0")

def sort(width: float, height: float, length: float, mass: float) -> str:
    check_inputs([width, height, length, mass])
    is_bulky, is_heavy = False, False
    volume = volume_calc(width, height, length)
    if volume >= 1000000:
        is_bulky = True
    if has_bulky_dimension([width, height, length]):
        is_bulky = True
    if has_heavy_mass(mass):
        is_heavy = True
    if all([is_bulky, is_heavy]):
        return StackEnum.REJECTED
    if any([is_bulky, is_heavy]):
        return StackEnum.SPECIAL
    return StackEnum.STANDARD
    