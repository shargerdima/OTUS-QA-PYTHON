import pytest
from src.Triangle import Triangle
from tests.conftest import square


def test_triangle_has_name(triangle):
    assert Triangle.get_name(triangle) == 'Triangle'


def test_triangle_area_is_correct(triangle):
    assert Triangle.get_area(triangle) == 0.0


def test_triangle_perimeter_is_correct(triangle):
    assert Triangle.get_perimeter(triangle) == 15


def test_triangle_add_area_circle(triangle, circle):
    assert triangle.add_area(circle) == 78.53981633974483


def test_triangle_add_area_invalid_class(triangle, rectangle):
    with pytest.raises(ValueError):
        triangle.add_area(square)
