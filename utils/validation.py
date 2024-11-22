from typing import Tuple, List


def validate_number_value(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be numbers.")


def validate_string_value(value):
    if not isinstance(value, str):
        raise TypeError("Value must be string.")


def validate_point(point: Tuple[float, float, float] | List[float, float, float]):
    if not isinstance(point, (tuple, list)):
        raise TypeError("First argument must be a point tuple (x, y)")
    if len(point) != 3:
        raise ValueError("Points must have exactly 3 coordinates")
