import pytest
from src.Circle import Circle
from tests.conftest import square


def test_circle_has_name(circle):
    assert Circle.get_name(circle) == 'Circle'


def test_circle_area_is_correct(circle):
    assert Circle.get_area(circle) == 78.53981633974483


def test_circle_perimeter_is_correct(circle):
    assert Circle.get_perimeter(circle) == 31.41592653589793


def test_circle_add_area_rectangle(circle, rectangle):
    assert circle.add_area(rectangle) == 88.53981633974483


def test_circle_add_area_invalid_class(circle, rectangle):
    with pytest.raises(ValueError):
        circle.add_area(square)