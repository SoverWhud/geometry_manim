from typing import Tuple
import utils

class Label:
    def __init__(self, text: str, position: Tuple[float, float, float], base_font_size: int = 36):
        """
            Initialize a Label object with text and position

            Args:
                text (str): The text content of the label.
                position (Tuple[float, float, float]): 3D coordinates position of the label.

            Example:
                # Create a label at position (10.5, 20.0, 5.5) with text "Hello"
                label = Label("Hello", (10.5, 20.0, 5.5))

            Raises:
                TypeError: If position is not a tuple/list or text is not a string.
                ValueError: If position does not contain exactly 3 coordinates.
            """
        utils.validate_point(position)

        self.text = text
        self._position = position

    @property
    def text(self) -> str:
        return self._text

    @property
    def position(self) -> Tuple[float, float, float]:
        return self._position

    @text.setter
    def text(self, value: str):
        utils.validate_string_value(value)
        self._text = value
