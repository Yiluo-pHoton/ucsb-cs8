#   Starting point for lab07, CMPSC 8, M17
import pytest

##############

from lab07 import isList

def test_isList_1():
    assert isList([])==True

def test_isList_2():
    assert isList([1])==True

def test_isList_3():
    assert isList([1,2,3])==True

def test_isList_4():
    assert isList([[1,2],"3"])==True

def test_isList_5():
    assert isList("3")==False

def test_isList_6():
    assert isList((1,2,3))==False

########

from lab07 import largestInt

def test_largestInt_01():
  with pytest.raises(ValueError):
    result= largestInt("not a list")

def test_largestInt_02():
  with pytest.raises(ValueError):
    result= largestInt([])

def test_largestInt_03():
  with pytest.raises(ValueError):
    result= largestInt(["foo",1,2])

def test_largestInt_04():
  with pytest.raises(ValueError):
    result= largestInt([1,"foo",2])
    
def test_largestInt_05():
  with pytest.raises(ValueError):
    result= largestInt([1,2,"foo"])
    
def test_largestInt_06():
  assert largestInt([1])==1

def test_largestInt_07():
  assert largestInt([2,3,4])==4

def test_largestInt_08():
  assert largestInt([7,6,5])==7
  
def test_largestInt_09():
  assert largestInt([6,9,5])==9
  
def test_largestInt_10():
  assert largestInt([-3,-2,-1])==-1
  
def test_largestInt_11():
  assert largestInt([3,3,3,3])==3

###############################

from lab07 import indexOfLargestInt

def test_indexOfLargestInt_01():
  with pytest.raises(ValueError):
    result= indexOfLargestInt("not a list")

def test_indexOfLargestInt_02():
  with pytest.raises(ValueError):
    result= indexOfLargestInt([])

def test_indexOfLargestInt_03():
  with pytest.raises(ValueError):
    result= indexOfLargestInt(["foo",1,2])

def test_indexOfLargestInt_04():
  with pytest.raises(ValueError):
    result= indexOfLargestInt([1,"foo",2])
    
def test_indexOfLargestInt_05():
  with pytest.raises(ValueError):
    result= indexOfLargestInt([1,2,"foo"])
    
def test_indexOfLargestInt_06():
  assert indexOfLargestInt([1])==0

def test_indexOfLargestInt_07():
  assert indexOfLargestInt([2,3,4])==2

def test_indexOfLargestInt_08():
  assert indexOfLargestInt([7,6,5])==0
  
def test_indexOfLargestInt_09():
  assert indexOfLargestInt([6,9,5])==1
  
def test_indexOfLargestInt_10():
  assert indexOfLargestInt([-3,-2,-1])==2
  
def test_indexOfLargestInt_11():
  assert indexOfLargestInt([3,3,3,3])==0

def test_indexOfLargestInt_11():
  assert indexOfLargestInt([2,3,3,3])==1

def test_indexOfLargestInt_12():
  assert indexOfLargestInt([2,1,3,3])==2

##########################

from lab07 import smallestInt



def test_smallestInt_01():
  with pytest.raises(ValueError):
    result= smallestInt("not a list")

def test_smallestInt_02():
  with pytest.raises(ValueError):
    result= smallestInt([])

def test_smallestInt_03():
  with pytest.raises(ValueError):
    result= smallestInt(["foo",1,2])

def test_smallestInt_04():
  with pytest.raises(ValueError):
    result= smallestInt([1,"foo",2])
    
def test_smallestInt_05():
  with pytest.raises(ValueError):
    result= smallestInt([1,2,"foo"])
    
def test_smallestInt_06():
  assert smallestInt([1])==1

def test_smallestInt_07():
  assert smallestInt([2,3,4])==2

def test_smallestInt_08():
  assert smallestInt([7,6,5])==5
  
def test_smallestInt_09():
  assert smallestInt([6,9,5])==5
  
def test_smallestInt_10():
  assert smallestInt([-3,-2,-1])==-3
  
def test_smallestInt_11():
  assert smallestInt([3,3,3,3])==3



#################################

from lab07 import indexOfSmallestInt

def test_indexOfSmallestInt_01():
  with pytest.raises(ValueError):
    result= indexOfSmallestInt("not a list")

def test_indexOfSmallestInt_02():
  with pytest.raises(ValueError):
    result= indexOfSmallestInt([])

def test_indexOfSmallestInt_03():
  with pytest.raises(ValueError):
    result= indexOfSmallestInt(["foo",1,2])

def test_indexOfSmallestInt_04():
  with pytest.raises(ValueError):
    result= indexOfSmallestInt([1,"foo",2])
    
def test_indexOfSmallestInt_05():
  with pytest.raises(ValueError):
    result= indexOfSmallestInt([1,2,"foo"])
    
def test_indexOfSmallestInt_06():
  assert indexOfSmallestInt([1])==0

def test_indexOfSmallestInt_07():
  assert indexOfSmallestInt([2,3,4])==0

def test_indexOfSmallestInt_08():
  assert indexOfSmallestInt([7,6,5])==2
  
def test_indexOfSmallestInt_09():
  assert indexOfSmallestInt([6,9,5])==2
  
def test_indexOfSmallestInt_10():
  assert indexOfSmallestInt([-3,-2,-1])==0
  
def test_indexOfSmallestInt_11():
  assert indexOfSmallestInt([3,3,3,3])==0

def test_indexOfSmallestInt_11():
  assert indexOfSmallestInt([2,3,3,3])==0

def test_indexOfSmallestInt_12():
  assert indexOfSmallestInt([2,1,1,3])==1

def test_indexOfSmallestInt_13():
  assert indexOfSmallestInt([-3,-5,-1])==1

def test_indexOfSmallestInt_14():
  assert indexOfSmallestInt([-3,-5,-1,-8])==3

################################

from lab07 import longestString

def test_longestString_01():
  with pytest.raises(ValueError):
    result= longestString("not a list")

def test_longestString_02():
  with pytest.raises(ValueError):
    result= longestString([])

def test_longestString_03():
  with pytest.raises(ValueError):
    result= longestString(["foo",1,2])

def test_longestString_04():
  with pytest.raises(ValueError):
    result= longestString([1,"foo",2])
    
def test_longestString_05():
  with pytest.raises(ValueError):
    result= longestString([1,2,"foo"])

def test_longestString_06():
  with pytest.raises(ValueError):
    result= longestString("foo")

    
def test_longestString_07():
  assert longestString(["foo","bar"])=="foo"

def test_longestString_08():
  assert longestString(["foo","bear"])=="bear"

def test_longestString_09():
  assert longestString(["foo","bear","bar"])=="bear"  

def test_longestString_10():
  assert longestString(["foo","wolf","bar","bear"])=="wolf"  

def test_longestString_11():
  assert longestString(["foo","wolf","bar","rabbit","bear"])=="rabbit"

def test_longestString_12():
  assert longestString(["wolf","bar","horse","bear","tiger"])=="horse"  

############

from lab07 import indexOfShortestString

def test_indexOfShortestString_01():
  with pytest.raises(ValueError):
    result= indexOfShortestString("not a list")

def test_indexOfShortestString_02():
  with pytest.raises(ValueError):
    result= indexOfShortestString([])

def test_indexOfShortestString_03():
  with pytest.raises(ValueError):
    result= indexOfShortestString(["foo",1,2])

def test_indexOfShortestString_04():
  with pytest.raises(ValueError):
    result= indexOfShortestString([1,"foo",2])
    
def test_indexOfShortestString_05():
  with pytest.raises(ValueError):
    result= indexOfShortestString([1,2,"foo"])

def test_indexOfShortestString_06():
  with pytest.raises(ValueError):
    result= indexOfShortestString("foo")

    
def test_indexOfShortestString_07():
  assert indexOfShortestString(["foo","bar"])==0

def test_indexOfShortestString_08():
  assert indexOfShortestString(["bear","foo"])==1

def test_indexOfShortestString_09():
  assert indexOfShortestString(["foo","bear","bar"])==0

def test_indexOfShortestString_10():
  assert indexOfShortestString(["foo","wolf","bar","bear"])==0

def test_indexOfShortestString_11():
  assert indexOfShortestString(["rabbit","wolf","rabbit","bear","foo"])==4

def test_indexOfShortestString_12():
  assert indexOfShortestString(["horse","rabbit","bear","tiger"])==2
