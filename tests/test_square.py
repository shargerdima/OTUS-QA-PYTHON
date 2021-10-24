import pytest
from src.Square import Square
from tests.conftest import triangle


def test_square_has_name(square):
    assert Square.get_name(square) == 'Square'


def test_square_area_is_correct(square):
    assert Square.get_area(square) == 16


def test_square_perimeter_is_correct(square):
    assert Square.get_perimeter(square) == 16


def test_square_add_area_triangle(square, triangle):
    assert square.add_area(triangle) == 16.0


def test_square_add_area_invalid_class(square, rectangle):
    with pytest.raises(ValueError):
        square.add_area(triangle)
