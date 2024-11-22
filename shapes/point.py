from typing import Tuple
import utils


class Point:
    def __init__(self, position: Tuple[float, float, float]):
        """
        Initialize a point with 3 coordinates.

        Args:
            position (tuple): Point coordinates (x, y, z)

        Example:
            # Initialize point with 3 coordinates
            point = Point((0, 0, 0))

        Raises:
            TypeError: If arguments have incorrect types
            ValueError: If point tuple doesn't contain exactly 3 coordinates
        """
        utils.validate_point(position)

        self._position = position

    @property
    def position(self) -> Tuple[float, float, float]:
        return self._position
