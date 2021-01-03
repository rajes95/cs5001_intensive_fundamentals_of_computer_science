# Author:  Maria Jump
# Version: 2019-02-08

import moreShapes


def readInteger(prompt, error="Value must be a positive integer"):
    """ Read and return a positive integer from keyboard """
    value = -1
    while(value == -1):
        entered = input(prompt)
        try:
            value = int(entered)
            if value <= 0:
                print(error)
                value = -1
        except ValueError:
            print(error)
            value = -1
    return value


def menu():
    """ Display the menu and read in user's choice """
    print()
    print("1 - Lower-Right Triangle")
    print("2 - Upper-Right Triangle")
    print("3 - Right Arrowhead")
    print("4 - Boomerang")
    print("5 - Diamond")
    print("6 - Exit")
    choice = -1
    while(choice == -1):
        error = "Valid options are between 1 and 6"
        choice = readInteger("Enter choice: ", error)
        if choice < 1 or choice > 6:
            print(error)
            choice = -1
    print()
    return choice


def main():
    choice = menu()
    while choice != 6:
        if choice == 1:
            size = readInteger("Enter size: ")
            moreShapes.printLowerRight(size)

        elif choice == 2:
            size = readInteger("Enter size: ")
            moreShapes.printUpperRight(size)

        elif choice == 3:
            size = readInteger("Enter size: ")
            moreShapes.printRightArrowhead(size)

        elif choice == 4:
            size = readInteger("Enter size: ")
            moreShapes.printBoomerang(size)

        elif choice == 5:
            error = "Sizes must be odd integers"
            size = readInteger("Enter size: ", error)
            while size % 2 == 0:
                print(error)
                size = readInteger("Enter size: ", error)
            moreShapes.printDiamond(size)

        # read another choice
        choice = menu()


if __name__ == "__main__":
    main()
