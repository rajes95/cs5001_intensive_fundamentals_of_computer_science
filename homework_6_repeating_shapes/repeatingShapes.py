# Author: Rajesh Sakhamuru
# Version: 2-20-2019


def printCheckerboard(size, width, height):
    """Prints a checkerboard shape of specified square size, and board size."""
    for h in range(height):
        if (h - 1) % 2 != 0:
            for n in range(size):
                for i in range(width):
                    if (i - 1) % 2 != 0:
                        print("*" * size, end="")
                    else:
                        print(" " * size, end="")
                print()
        else:
            for n in range(size):
                for i in range(width):
                    if (i - 1) % 2 != 0:
                        print(" " * size, end="")
                    else:
                        print("*" * size, end="")
                print()


def printBoxGrid(size, width, height):
    """Draws a grid of square boxes of specified size and specified
    width and height of grid."""
    for r in range(((size + 1) * height) + 1):
        if r % (size + 1) == 0:
            for i in range(((size + 1) * width) + 1):
                print("*", end="")
            print()
        else:
            for i in range(width):
                print("*" + (" " * size), end="")
            print("*")


def printTrianglePattern(size, width, height):
    """Prints a Lower Left Aligned triangle grid of spefied size and specified
    grid width and height."""
    for i in range(height):
        for r in range(size):
            print((("*" * (r + 1)) + (" " * (size - (r)))) * width)


def printDiamondPattern(size, width, height):
    """Prints a Diamond pattern with diamond of specified size and a specified
    width and height for the grid of diamonds."""
    for i in range(height):
        space1 = int((size - 1) / 2)
        star1 = size - 2 * int((size - 1) / 2)
        for r in range(size):
            if r < int(size / 2) + 1:
                print((" " * (space1) + "*" * (star1) + " " * (space1 + 1)) * width)
                space1 -= 1
                star1 += 2
            else:
                space1 += 1
                star1 -= 2
                if (r + 1) != size:
                    print((" " * (space1 + 1) + "*" * (star1 - 2) + " " * (space1 + 2)) * width)
    if size != 1:
        print((" " * (space1 + 1) + "*" * (star1 - 2) + " " * (space1 + 2)) * width)
