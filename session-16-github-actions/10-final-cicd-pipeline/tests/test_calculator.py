import sys
import os
import pytest

# Ensure app module can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.calculator import add, subtract, multiply, divide, power, modulo


def test_add():
    assert add(10, 5) == 15
    assert add(-3, 3) == 0
    assert add(2.5, 3.5) == 6.0


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5
    assert subtract(0, 0) == 0


def test_multiply():
    assert multiply(10, 5) == 50
    assert multiply(-4, 5) == -20
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 5) == 2
    assert divide(9, 2) == 4.5
    assert divide(-10, 2) == -5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(15, 5) == 0


def test_modulo_by_zero():
    with pytest.raises(ValueError, match="Cannot perform modulo with zero divisor"):
        modulo(10, 0)
