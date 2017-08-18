import pytest

def perimRect(length, width):
    """
    Computer perimeter for the rectangle
    """
    return 2 * (length +  width)

def test_perimRect_1():
    assert perimRect(2, 2) == 8

def test_perimRect_2():
    assert perimRect(1, 3) == 8

def test_perimRect_3():
    assert perimRect(1.2, 4.4) == pytest.approx(11.2)

def test_perimRect_4():
    assert perimRect(0.4, 11.2) == pytest.approx(23.2)

def areaRect(length, width):
    """
    Compute area for the rectangle
    """
    return length * width

def test_areaRect_1():
    assert areaRect(2, 2) == 4

def test_areaRect_2():
    assert areaRect(1.3, 1.9) == pytest.approx(2.47)

def test_areaRect_3():
    assert areaRect(3, 4.2) == pytest.approx(12.6)
