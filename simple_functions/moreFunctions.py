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


def star(value1, value2):
    product = value1 * value2
    return product


def reformatName(firstName, lastName):
    firstName = firstName.lower()
    firstName = firstName.capitalize()
    lastName = lastName.upper()
    fullName = firstName + " " + lastName
    return fullName
