# Author: Rajesh Sakhamuru
# Version: 1/26/2019


def xor(x, y):
    """
    GIVEN: x and y as boolean variables
    WHEN: xor(x, y) is called
    THEN: the function xor determines whether x or y are true, but not both
          in other words, indicating whether they satisfy the "exclusive or"
          by returning True or False.
    """
    if ((x and (not y)) or (y and (not x))):
        return True
    return False


def isNegative(value):
    """
    GIVEN: a numerical value "value"
    WHEN: isNegative(value) is called
    THEN: True is returned if the value is Negative, and False
          if the value is Positive or equal to 0.
    """
    if value < 0:
        return True
    return False


def isLeapYear(year):
    """
    GIVEN: variable year, which is an integer value indicating a particular year
    WHEN: isLeapYear(year) is called
    THEN: if year is a leap year, True is returned, otherwise False is returned
    """
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    return False
