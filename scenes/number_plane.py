from manim import *

line_style = {
    "stroke_color": TEAL,
    "stroke_width": 4,
    "stroke_opacity": 0.6
}


class CreateNumberPlane(Scene):
    def construct(self):
        # Calculation of screen sizes in Manim units
        screen_width = config.frame_width
        screen_height = config.frame_height

        # Determining ranges based on aspect ratio
        x_min, x_max = -screen_width / 2, screen_width / 2
        y_min, y_max = -screen_height / 2, screen_height / 2

        plane = NumberPlane(
            x_range=[x_min, x_max, 1],  # Step 1 to match the units exactly
            y_range=[y_min, y_max, 1],
            x_length=screen_width,
            y_length=screen_height,
            background_line_style=line_style,
        )

        plane.center()
        self.add(plane)