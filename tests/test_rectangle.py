import pytest
from src.Rectangle import Rectangle
from tests.conftest import square


def test_rectangle_has_name(rectangle):
    assert Rectangle.get_name(rectangle) == 'Rectangle'


def test_rectangle_area_is_correct(rectangle):
    assert Rectangle.get_area(rectangle) == 10


def test_rectangle_perimeter_is_correct(rectangle):
    assert Rectangle.get_perimeter(rectangle) == 14


def test_rectangle_add_area_square(rectangle, square):
    assert rectangle.add_area(square) == 26.0


def test_rectangle_add_area_invalid_class(rectangle, circle):
    with pytest.raises(ValueError):
        rectangle.add_area(square)