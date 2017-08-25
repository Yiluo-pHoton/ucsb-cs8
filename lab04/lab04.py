#!/usr/bin/env python3
import convert
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        fTempStr = sys.argv[1]
    else:
        fTempStr = input("Please enter a Fahrenheit temperature: ")
    print("You entered: " + fTempStr)
    
    try:
        fTemp = float(fTempStr)
        cTemp = convert.fToC(fTemp)
        print("{} degrees F = {} degrees C".format(fTemp, cTemp))
    except ValueError:
        print("Sorry, I could not convert {} to a number".format(fTempStr))

