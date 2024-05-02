import pytest

from ..calculator import add, subtract, multiply, divide

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(0, 0) == 0
    assert multiply(-1, -1) == 1
    assert multiply(-1, 1) == -1

def test_divide():
    assert divide(1, 2) == 0.5
    assert divide(0, 1) == 0
    assert divide(-1, -1) == 1
    assert divide(-1, 1) == -1

    with pytest.raises(ValueError):
        divide(1, 0)
