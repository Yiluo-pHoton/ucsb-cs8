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

#rectangle area
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

#is string
def isString(obj):
    return (type(obj) == str)

def test_isString_1():
    assert isString("asdf")

def test_isString_2():
    assert isString("sa7890")

def test_isString_3():
    assert not isString(56789)

def test_isString_4():
    assert not isString(12)

def test_isString_5():
    assert isString("")

#is number
def isNumber(obj):
    return (type(obj) == int or type(obj) == float)

def test_isNumber_1():
    assert isNumber(1234)

def test_isNumber_2():
    assert isNumber(890.123)

def test_isNumber_3():
    assert not isNumber("asdf")

def test_isNumber_4():
    assert not isNumber([789, 67890, 123])

def test_isNumber_5():
    assert not isNumber("yui")

