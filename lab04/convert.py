import math
import pytest

if __name__ == '__main__':
    print('This is the main block of convert.py')

def fToC(temp):
    return (temp - 32) / 1.8

def cToF(temp):
    return temp * 1.8 + 32

def test_fToC_freezing():
   assert fToC(32.0)==pytest.approx(0.0) 

def test_cToF_freezing():
   assert cToF(0.0)==pytest.approx(32.0) 

def test_fToC_boiling():
   assert fToC(212.0)==pytest.approx(100.0) 

def test_cToF_boiling():
   assert cToF(100.0)==pytest.approx(212.0) 
