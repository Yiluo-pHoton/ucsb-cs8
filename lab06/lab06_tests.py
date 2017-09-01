# tests for lab06, UCSB, CMPSC 8, Summer 2017
# Instructor: P. Conrad



from lab06 import notStringContainingE

def test_notStringContainingE_1():
   assert notStringContainingE('Fred')==False

def test_notStringContainingE_2():
   assert notStringContainingE('Jane')==False

def test_notStringContainingE_3():
   assert notStringContainingE('Santa')==True

def test_notStringContainingE_4():
   assert notStringContainingE('Barbara')==True

def test_notStringContainingE_5():
   assert notStringContainingE('Edward')==False

def test_notStringContainingE_6():
   assert notStringContainingE('Ice Cream')==False

def test_notStringContainingE_7():
   assert notStringContainingE(23)==True
   
def test_notStringContainingE_8():
   assert notStringContainingE(['e'])==True
   
###########################

from lab06 import hasNoX

def test_hasNoX_1():
   assert hasNoX('Fred')==True

def test_hasNoX_2():
   assert hasNoX('Xerox')==False

def test_hasNoX_3():
   assert hasNoX('Box')==False

def test_hasNoX_4():
   assert hasNoX('Xbox')==False

def test_hasNoX_5():
   assert hasNoX(23)==True

def test_hasNoX_6():
   assert hasNoX(['x'])==True

def test_hasNoX_7():
   assert hasNoX('x')==False

###################

from lab06 import isNumber

def test_isNumber_1():
   assert not isNumber("UCSB")

def test_isNumber_2():
   assert isNumber(42)

def test_isNumber_3():
   assert not isNumber(["UCSB"])

def test_isNumber_4():
   assert isNumber(-3.4)

def test_isNumber_5():
   assert not isNumber(("UCSB","UCLA"))

##########################################
   
from lab06 import isListOfNumber

def test_isListOfNumber_1():
   assert isListOfNumber('Fred')==False
   
def test_isListOfNumber_2():
   assert isListOfNumber(3)==False
   
def test_isListOfNumber_3():
   assert isListOfNumber([3])==True
   
def test_isListOfNumber_4():
   assert isListOfNumber([3.4])==True

def test_isListOfNumber_5():
   assert isListOfNumber([2,3,4,5.6,7])==True

def test_isListOfNumber_6():
   assert isListOfNumber([2,3,'oops',5])==False

def test_isListOfNumber_7():
   assert isListOfNumber([2,3,[4]])==False

def test_isListOfNumber_8():
   assert isListOfNumber([])==True

#######################
from lab06 import isListOfIntegers

def test_isListOfIntegers_1():
   assert isListOfIntegers('Fred')==False


def test_isListOfIntegers_2():
   assert isListOfIntegers(3)==False


def test_isListOfIntegers_3():
   assert isListOfIntegers([3])==True


def test_isListOfIntegers_4():
   assert isListOfIntegers([3.4])==False


def test_isListOfIntegers_5():
   assert isListOfIntegers([2,3,4,5.6,7])==False


def test_isListOfIntegers_6():
   assert isListOfIntegers([2,3,'oops',5])==False


def test_isListOfIntegers_7():
   assert isListOfIntegers([2,3,4,5,6,7])==True


def test_isListOfIntegers_8():
   assert isListOfIntegers([2,3,[4]])==False


def test_isListOfIntegers_9():
   assert isListOfIntegers([])==True


#############
from lab06 import isListOfEvenIntegers

def test_isListOfEvenIntegers_1():
   assert isListOfEvenIntegers('Fred')==False


def test_isListOfEvenIntegers_2():
   assert isListOfEvenIntegers(3)==False


def test_isListOfEvenIntegers_3():
   assert isListOfEvenIntegers([3])==False


def test_isListOfEvenIntegers_4():
   assert isListOfEvenIntegers([4])==True


def test_isListOfEvenIntegers_5():
   assert isListOfEvenIntegers([3.4])==False


def test_isListOfEvenIntegers_6():
   assert isListOfEvenIntegers([2,3,4,5.6,7])==False


def test_isListOfEvenIntegers_7():
   assert isListOfEvenIntegers([2,3,'oops',5])==False


def test_isListOfEvenIntegers_8():
   assert isListOfEvenIntegers([2,3,4,5,6,7])==False


def test_isListOfEvenIntegers_9():
   assert isListOfEvenIntegers([2,4,6])==True


def test_isListOfEvenIntegers_10():
   assert isListOfEvenIntegers([2,3,[4]])==False


def test_isListOfEvenIntegers_11():
   assert isListOfEvenIntegers([])==True

###########
