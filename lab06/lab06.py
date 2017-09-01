# tests for lab06, UCSB, CMPSC 8, Summer 2017
# Instructor: P. Conrad
# Student(s): Yiluo Li 

# @@@ This next function has an error.  Can you fix it?
# @@@ Hint: you might need to use the "and" or "or" keywords of python
# @@@ and modify the if test.

def notStringContainingE(word):
    """
    return True when word is a string that contains no letter 'e' (or 'E')
    It should work both for lower and upper case.
    When word isn't a string, return True 
    (because it is not a string contaning an E)
    """
   
    if not(type(word)==str):
        return True
    for letter in word:
        if letter.lower() == 'e':   
            return False
    return True

#@@@ Here is a function definition that doesn't pass one or more of its tests.
#@@@ Fix it!  (Also try to understand why it is wrong)

def hasNoX(word):
    """
    return True when word is a string that contains no letter 'x' 
    (and no letter 'X')
    It should work both for lower and upper case.
    When word isn't a string, return True (because it is not a string 
    with an  x in that case!)
    """
    if (type(word)!=str):
        return True
    for letter in word:
        if letter == 'x' or letter == 'X':
            return False
    return True


# The follwing function is provided for you as an example
# of how to write a Python function that checks if EVERY element
# of a list has some property.


def isNumber(item):
    "return True if item is of type int or type float otherwise False "
    if type(item) == float or type(item) == int:
        return True
    return False   

def isListOfNumber(theList):
   """
   indicates whether value of argument is a list of only simple numbers
   (int or float) 
   Note: empty list should return True---it doesn't contain anything that 
   ISN'T a simple number
   theList can be anything, and the function will return either True or False.
   """

   if not type(theList)==list:
      return False  # it isn't really a list!

   # Now we can assume that theList really is a list
   # But is it a list of all numerics?
   # If we find even a single item that isn't numeric, we can
   # immediately return false.  
   
   for item in theList:
     if not isNumber(item):
       return False

   # If we get here and didn't return yet, then we know everything
   # in the list is a simple numeric!
   # (i.e. there isn't anything in the list that is NOT simple numeric)
   
   return True

### @@@ NOW, write a function called isListOfIntegers(x)
### @@@ The function should take anything as an argument, and produce True
### @@@   only if argument is a list consisting of only int values 
### @@@ similar to the comments above the other function definitions in this file
### @@@ See previous function for a clue as to how to proceed
### @@@ Note that empty list should return True (for same reasoning as in the previous function)

def isListOfIntegers(theList):
    """
    indicates whether value of argument is a list of only int 
    Note: empty list should return True
    because it doesn't contain anything that ISN'T int
    theList can be anything, and it will return either True or False.
    """
    if type(theList) != list:
        return False
    for i in theList:
        if type(i) != int:
            return False
    return True

### @@@ NOW, write a function called isListOfEvenIntegers(x)
### @@@ The function should take anything as an argument, and produce True
### @@@   only if argument is a list consisting of only int values that
### @@@   are even.  See previous function for a clue as to how to proceed
### @@@ Note that empty list should return True

### @@@ HINT: to avoid problems when using the % operator
### @@@ (that's another hint), use your isListOfIntegers function first.
### @@@ This is sort of like the way that isListOfSimpleNumeric
### @@@ checks first to see if theList is a list.
### @@@ That way, you kill two birds with one stone---you immediately
### @@@ know that you are working with a list of integers, and you
### @@@ only have to worry about whether all of them are even or not.

def isListOfEvenIntegers(theList):
    """
    indicates whether value of argument is a list of only even integers
    Note: empty list should return True---it doesn't contain anything that 
    ISN'T an even integer
  
    theList can be anything, and it will return either True or False.
    """
    if not isListOfIntegers(theList):
        return False
    for i in theList:
        if i % 2 != 0:
            return False
    return True      

### @@@ NOW, write a function called totalLength(x)
### @@@   Use the accumulator pattern to compute the total length
### @@@   of all the words in a string
### @@@   The accumulator will be an integer that starts at zero.
### @@@   You'll use a for loop to look at each item in the list


def totalLength(listOfStrings):
    """
    returns total length of all the strings in a list of strings, 
    False if argument not a list, 0 for empty list
    """
    if listOfStrings:
return "stub" 