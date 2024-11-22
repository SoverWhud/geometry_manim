from manim import *
import os

from scenes.number_plane import CreateNumberPlane


class Main(Scene):
    def construct(self):
        all_scenes = [CreateNumberPlane]

        for cls in all_scenes:
            cls.construct(self)


if __name__ == '__main__':
    with tempconfig({
        "frame_width": 16,
        "frame_height": 9,
        "output_file": os.path.splitext(os.path.basename(__file__))[0],
        "disable_caching": True
    }):
        scene = Main()
        scene.render()
