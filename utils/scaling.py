from manim import *


class ScalingManager:
    """
    Manages scaling of scene elements to adapt to rendering window dimensions.

    Attributes:
        scene (Scene): Manim scene for visualization
        frame_width (int): Frame width from Manim configuration
        frame_height (int): Frame height from Manim configuration
        min_dimension (int): Minimum dimension for correct scaling
    """

    def __init__(self, scene: Scene):
        """
        Initializes the scaling manager.

        Args:
            scene (Scene): Manim scene for which scaling is performed

        Remarks:
            Uses global Manim configuration to determine frame dimensions
        """
        self.scene = scene
        # Get the dimensions of the rendering area
        self.frame_width = config.frame_width
        self.frame_height = config.frame_height
        # Determine the minimum size for scaling
        self.min_dimension = min(self.frame_width, self.frame_height)

    def get_scaled_size(self, base_size: float) -> float:
        """Scales the size relative to the window size"""
        return base_size * (self.min_dimension / 8)  # 8 - это базовый делитель для удобного масштаба
