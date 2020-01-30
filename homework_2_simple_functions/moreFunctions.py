# Author: Rajesh Sakhamuru
# Version: 1/20/2019


def printFlag():
    print((("*" + " ") * 5) + ("R" * 20))
    print((("*" + " ") * 5) + (" " * 20))
    print((("*" + " ") * 5) + ("R" * 20))
    print((("*" + " ") * 5) + (" " * 20))
    print("R" * 30)
    print(" " * 30)
    print("R" * 30)
    print(" " * 30)
    print("R" * 30)

""" # I wrote this program before the instructions were clarified on Piazza
def printFlag():
    lines = 0
    while lines < 2:
        count = 0
        while count < 5:
            print("*", end='')
            print(" ", end='')
            count += 1
        red = 0
        while red < 19:
            print("R", end='')
            red += 1
        print('')
        count = 0
        while count < 5:
            print("*", end='')
            print(" ", end='')
            count += 1
        print('')
        lines += 1
    lines = 0
    while lines < 3:
        red = 0
        while red < 29:
            print("R", end='')
            red += 1
        print('')
        if lines != 2:
            print('')
        lines += 1
"""


def star(value1, value2):
    product = value1 * value2
    return product


def reformatName(firstName, lastName):
    firstName = firstName.lower()
    firstName = firstName.capitalize()
    lastName = lastName.upper()
    fullName = firstName + " " + lastName
    return fullName
