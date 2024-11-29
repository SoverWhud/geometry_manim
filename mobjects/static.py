import shapes
import manim


def create_point_mobject(point, scale, **kwargs):
    if type(point) is not shapes.Point:
        raise TypeError("Shape is not Point")

    return manim.Dot(point=point.position, **kwargs).scale(scale)


def create_label_mobjects(shape, font_size, **kwargs):
    if type(shape) is not shapes.Label:
        raise TypeError("Shape is not Label")

    return manim.Text(shape.text, font_size=font_size, **kwargs).move_to(shape.position)