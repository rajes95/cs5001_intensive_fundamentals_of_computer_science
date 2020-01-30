# Author:  Rajesh Sakhamuru
# Version: 2/10/2019


def printLowerRight(size):
    """
    This function prints a right-aligned triangle with an incrementing number of "*" in each
    row until it reaches the specified size. A Lower Right triangle of size 6 would
    look like this:
         *
        **
       ***
      ****
     *****
    ******
    """
    row = 0
    count = size
    col = 0
    while row < size:
        while col < (count - 1):
            print(" ", end="")
            col += 1
        print("*" * (row + 1), end="")
        print()
        count -= 1
        col = 0
        row += 1


def printUpperRight(size):
    """
    This function prints a right aligned triangle with a decrementing number of "*" in each
    row until it reaches 1 from the specified size. An Upper Right Triangle of size 8 would
    look like this:
    ********
     *******
      ******
       *****
        ****
         ***
          **
           *
    """
    col = size
    row = size
    count = size
    while row > 0:
        while col < size:
            print(" ", end="")
            col += 1
        print("*" * row, end="")
        print()
        count -= 1
        col = count
        row -= 1


def printRightArrowhead(size):
    """
    This function prints a right-aligned "arrowhead" with an incrementing by 1 number of "*" in each
    row until it reaches the specified size then decrements by 1 to a single "*".
    An right-Arrowhead of size 5 would look like this:
        *
       **
      ***
     ****
    *****
     ****
      ***
       **
        *
    """
    row = 0
    count = size
    col = 0
    while row < size:
        while col < (count - 1):
            print(" ", end="")
            col += 1
        print("*" * (row + 1), end="")
        print()
        count -= 1
        col = 0
        row += 1
    col = size - 1
    row = size - 1
    count = size - 1
    while row > 0:
        while col < size:
            print(" ", end="")
            col += 1
        print("*" * row, end="")
        print()
        count -= 1
        col = count
        row -= 1


def printBoomerang(size):
    """
    This function prints a "boomerang" shape with an incrementing by 1 number of "*" in each
    row until it reaches the specified size then decrements by 1 to a single "*".
    An boomerang of size 5 would look like this:
            *
          **
        ***
      ****
    *****
      ****
        ***
          **
            *
    """
    row = 0
    count = size
    col = 0
    while row < size:
        while col < (count - 1):
            print("  ", end="")
            col += 1
        print("*" * (row + 1), end="")
        print()
        count -= 1
        col = 0
        row += 1
    col = size - 1
    row = size - 1
    count = size - 1
    while row > 0:
        while col < size:
            print("  ", end="")
            col += 1
        print("*" * row, end="")
        print()
        count -= 1
        col = count
        row -= 1


def printDiamond(size):
    """
    This function prints a "diamond" shape with a number of rows indicated by
    the inputted size value. First row has one "*" and each subsequent row has 2
    more "*" in until the number of "*" equals the size value. Then in the
    next rows the number of "*" decrements by two until there is only 1 in the
    last row. This function only works with odd values for size. A diamond of
    size 9 would look like this:
        *
       ***
      *****
     *******
    *********
     *******
      *****
       ***
        *
    """
    row = 0
    count = int((size - 1) / 2)
    while row < (((size - 1) / 2) + 1):
        print(" " * count, end="")
        print("**" * (row) + "*", end="")
        print()
        count -= 1
        row += 1
    row = int((size - 1) / 2) - 1
    count = 0
    while row >= 0:
        print(" " * (count + 1), end="")
        print("**" * row + "*", end="")
        print()
        count += 1
        row -= 1
