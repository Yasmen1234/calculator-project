import pytest
from calculator import Calculator

calc=Calculator()


def test_add_positive():
    assert calc.add(5, 3) == 8

def test_add_negative():
    assert calc.add(-5, -3) == -8

def test_add_zero():
    assert calc.add(5, 0) == 5


def test_minus_positive():
    assert calc.subtract(5, 3) == 2

def test_minus_negative():
    assert calc.subtract(-5, -3) == -2

def test_minus_zero():
    assert calc.subtract(5, 0) == 5


def test_multiply_positive():
    assert calc.multiply(5, 3) == 15

def test_multiply_by_zero():
    assert calc.multiply(5, 0) == 0

def test_multiply_negative():
    assert calc.multiply(-5, 3) == -15


def test_divide_normal():
    assert calc.divide(6, 3) == 2

def test_divide_float():
    assert calc.divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(5, 0)