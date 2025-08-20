from typing import List
from enum import StrEnum
import sys


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

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python main.py <width> <height> <length> <mass>")
        print("Example: python main.py 100 100 100 20")
        sys.exit(1)
    
    try:
        width = float(sys.argv[1])
        height = float(sys.argv[2])
        length = float(sys.argv[3])
        mass = float(sys.argv[4])
        
        result = sort(width, height, length, mass)
        print(f"Package dimensions: {width} x {height} x {length} cm")
        print(f"Package mass: {mass} kg")
        print(f"Volume: {volume_calc(width, height, length)} cm³")
        print(f"Result: {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    