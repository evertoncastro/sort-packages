import pytest
from main import (
    volume_calc,
    has_bulky_dimension,
    has_heavy_mass,
    sort,
    StackEnum
)

def test_volume_calc():
    assert volume_calc(100, 100, 100) == 1000000
    assert volume_calc(100, 100, 99) == 990000
    assert volume_calc(1000, 1000, 1000) == 1000000000
    assert volume_calc(10, 20, 30) == 6000

def test_has_bulky_dimensions():
    assert has_bulky_dimension([1, 1, 150]) is True
    assert has_bulky_dimension([1, 1, 149]) is False
    assert has_bulky_dimension([100, 100, 100]) is False
    assert has_bulky_dimension([149, 149, 149]) is False
    assert has_bulky_dimension([150, 1, 1]) is True
    assert has_bulky_dimension([149.999, 1, 1]) is False
    assert has_bulky_dimension([1000, 1000, 1000]) is True
    assert has_bulky_dimension([0.001, 0.001, 0.001]) is False

def test_has_heavy_mass():
    assert has_heavy_mass(19) is False
    assert has_heavy_mass(21) is True
    assert has_heavy_mass(20) is True
    assert has_heavy_mass(19.999) is False
    assert has_heavy_mass(1000) is True
    assert has_heavy_mass(0.001) is False

def test_sort_conditions():
    assert sort(100, 100, 100, 19) == StackEnum.SPECIAL  # Bulky volume, not heavy
    assert sort(100, 100, 100, 20) == StackEnum.REJECTED  # Bulky volume + heavy
    assert sort(150, 10, 10, 19) == StackEnum.SPECIAL  # Bulky dimension, not heavy
    assert sort(150, 10, 10, 20) == StackEnum.REJECTED  # Bulky dimension + heavy
    assert sort(10, 10, 10, 20) == StackEnum.SPECIAL  # Heavy, not bulky

def test_sort_edge_cases():
    assert sort(0.001, 0.001, 0.001, 0.001) == StackEnum.STANDARD
    assert sort(1000, 1000, 1000, 100) == StackEnum.REJECTED
    assert sort(149, 149, 149, 19) == StackEnum.SPECIAL
    assert sort(151, 151, 151, 21) == StackEnum.REJECTED

def test_sort_inputs():
    with pytest.raises(ValueError):
        sort(0, 0.1, 0.1, 0.1)
    with pytest.raises(ValueError):
        sort(0.1, 0, 0.1, 0.1)
    with pytest.raises(ValueError):
        sort(0.1, 0.1, 0, 0.1)
    with pytest.raises(ValueError):
        sort(0.1, 0.1, 0.1, 0)
    with pytest.raises(ValueError):
        sort(-0.1, 0.1, 0.1, 0.1)
    with pytest.raises(ValueError):
        sort(0.1, -0.1, 0.1, 0.1)
    with pytest.raises(ValueError):
        sort(0.1, 0.1, -0.1, 0.1)
    with pytest.raises(ValueError):
        sort(0.1, 0.1, 0.1, -0.1)
