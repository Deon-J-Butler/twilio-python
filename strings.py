import sys


def excited(string):
    excited_string = (string.upper()+"!!!")
    return excited_string


userInput = str(sys.argv[1])

print(excited(userInput))
