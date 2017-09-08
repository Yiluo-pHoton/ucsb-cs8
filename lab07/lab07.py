
#   Starting point for lab07, CMPSC 8, M17
import pytest

# The following function is copied from lab05---as an example of how to
#  check for type, and because it is generally useful

def isList(x):
    """
    check whether parameter is a list
    """
    return type(x) == list


def largestInt(listOfInts):
    """
    return largest element of a list of ints, 
    raise ValueError if non empty, not a list, or not a list of ints
    
    By "largest", we mean a value that is no smaller than any other
      value in the list (There may be more than one instance of that
      value--e.g. in [7,3,7], 7 is largest      
    """
    
    if type(listOfInts)!=list:
       raise ValueError("argument to largestInt should be a list")
   
    if listOfInts==[]:
       raise ValueError("argument to largestInt may not be empty")

    # Now we know there is at least one item in the list.
    # We make an initial assumption that this item will be the largest.
    # We then check every other item in the list--each gets a chance to
    #  knock the maxSoFar out of the winner's circle

    maxSoFar = listOfInts[0]  # the one in position zero is best guess so far

    # Note: we have to start from 0 because we need to check the type
    #  of element[0] to see if it is an int.  Otherwise, we could start from 1
    
    for i in range(0,len(listOfInts)):  # all indexes in the list
        
       if type(listOfInts[i])!=int:      # make sure it is an int
          raise ValueError("element " + str(i) + " isn't an int")

       if listOfInts[i] > maxSoFar:  # compare the new item with maxSoFar
          maxSoFar = listOfInts[i]   # we have a new candidate
                                     # for the title of "largest int"

    # Now we've gone through the entire list.  Every other item on the list
    # has had a chance to defeat maxSoFar as the largest int.  So the one
    # left in maxSoFar must be the largest one.

    return maxSoFar


def indexOfLargestInt(listOfInts):
    """
    return index of largest element of a list of ints
    raise ValueError if non empty, not a list, or not a list of ints
    By "largest", we mean a value that is no smaller than any other 
    value in the list (see comment in definition of largestInt)
    By "index", we mean the subscript that will select that item of
    the list when placed in [].   Since there can be more than one
    largest, we'll return the index of the first such value in those
    cases, i.e. the one with the lowest index.
      
    """

    if type(listOfInts)!=list:
       raise ValueError("argument to largestInt should be a list")
    if listOfInts==[]:
       raise ValueError("argument to largestInt may not be empty")

    # Now we know there is at least one item in the list.
    # We make an initial assumption that this item will be the largest.
    # We then check every other item in the list--each gets a chance to
    #  knock the maxSoFar out of the winner's circle

    indexOfMaxSoFar = 0    # the one in position zero is the first candidate


    # Note: we have to start from 0 because we need to check the type
    #  of element[0] to see if it is an int.  Otherwise, we could start from 1
    
    for i in range(0,len(listOfInts)):  # all indexes in the list
        
       if type(listOfInts[i])!=int:      # make sure it is an int
          raise ValueError("element " + str(i) + " isn't an int")          

       if listOfInts[i] > listOfInts[indexOfMaxSoFar]:
           # compare the new item with maxSoFar
           indexOfMaxSoFar = i  # we have a new candidate; store the INDEX

    # Now we've gone through the entire list.  Every other item on the list
    # has had a chance to defeat maxSoFar as the largest int.  So the one
    # left in maxSoFar must be the largest one.

    return indexOfMaxSoFar




# @@@ NOW: complete the function below
# @@@  It will be similar to largestInt

def smallestInt(listOfInts):
    """
    return smallest element of a list of ints
    raise ValueError if non empty, not a list, or not a list of ints
    By "smallest", we mean a value that is no smaller than any 
    other value in the list
    """
    if type(listOfInts) != list:
        raise ValueError("Input value must be a list")
    if listOfInts == []:
        raise ValueError("Input list must not be empty")

    minInt = float('inf') 

    for i in range(len(listOfInts)):
        if type(listOfInts[i]) != int:
            raise ValueError("element " + str(i) + " isn't an int")
        if listOfInts[i] < minInt:
            minInt = listOfInts[i]
    return minInt


# @@@ NOW: complete the function below
# @@@  It will be similar to indexOfLargestInt

def indexOfSmallestInt(listOfInts):
    """
    return index of smallest element of a list of ints
    raise ValueError if non empty, not a list, or not a list of ints
    """
    minInt = smallestInt(listOfInts)
    return listOfInts.index(minInt)




# @@@ NOW: complete the function below
# @@@  You'll have to decide which of the models above fits
# @@@  Recall that len(s) returns the length of a string
# @@@  If you have a listOfStrings, then len(listOfStrings[i]))
# @@@  returns the length of the ith string in that list

def longestString(listOfStrings):
    """
    return longestString from a list of strings
    raise ValueError if non empty, not a list, or not a list of strings
    By "longest", we mean a value that is no shorter than any 
    other value in the list
    There may be more than one string that would qualify:
    For example in the list ["dog","bear","wolf","cat"] both bear and 
    wolf are longest strings
    In such cases, return the one with the lowest index (in this case, bear)  
        
    """
    if type(listOfStrings) != list:
        raise ValueError('It is not a list!')
    if listOfStrings == []:
        raise ValueError('It cannot be empty!')

    longest = ''

    for i in range(0, len(listOfStrings)):
        if type(listOfStrings[i]) != str:
            raise ValueError('element ' + str(i) + ' is not a string')
        if len(listOfStrings[i]) > len(longest):
            longest = listOfStrings[i]
    return longest



# @@@ NOW: complete the function below
# @@@  You'll have to decide which of the models above fits

def indexOfShortestString(listOfStrings):
    """
    return index of shortest string from a list of strings
    raise ValueError if non empty, not a list, or not a list of strings
    By "shortest", we mean a value that is no longer than any other 
    value in the list
    There may be more than one string that would qualify,
    For example in the list ["dog","bear","wolf","cat"] both dog and cat 
    are shortest strings
    
    In such cases, return the one with the lowest index (in this case, dog)  
    """
    longest = longestString(listOfStrings)
    shortest = listOfStrings[0]
    index = 0  
    for i in range(len(listOfStrings)):
        if len(listOfStrings[i]) < len(shortest):
            shortest = listOfStrings[i]
            index = i
    return index
