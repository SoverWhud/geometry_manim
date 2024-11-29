from manim import *
from typing import Tuple, Any


class ScalingManager:
    """
    Manages scaling of scene elements to adapt to rendering window dimensions.

    Attributes:
        frame_width (int): Frame width from Manim configuration
        frame_height (int): Frame height from Manim configuration
        scale (int): Scale factor
    """

    def __init__(self, frame_width: float, frame_height: float):
        """
        Initializes the scaling manager.

        Args:
            frame_width (int): Frame width from Manim configuration
            frame_height (int): Frame height from Manim configuration

        Remarks:
            Uses global Manim configuration to determine frame dimensions
        """
        # Get the dimensions of the rendering area
        self.frame_width = frame_width
        self.frame_height = frame_height

        # Determine the minimum size for scaling
        self.scale = min(self.frame_width, self.frame_height) / 8 # 8 is a base divisor for convenient scaling


    def get_scaled_size(self, base_size: float) -> float:
        """Scales the size relative to the window size"""
        return base_size * self.scale

    def get_scaled_point(self, base_point: Tuple[float | Any, ...]):
        """Scales the size relative to the window size"""
        return tuple(p * self.scale for p in base_point)

    def get_font_size(self, base_size: int = 36) -> int:
        """Calculates the font size relative to the window size"""
        return int(base_size * self.scale)
