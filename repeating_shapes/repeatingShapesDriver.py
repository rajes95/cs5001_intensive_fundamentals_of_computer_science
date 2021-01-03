# Author:  Maria Jump
# Version: 2019-02-15

import repeatingShapes


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
    print("1 - Checkerboard")
    print("2 - Box Grid")
    print("3 - Triangle Pattern")
    print("4 - Diamond Pattern")
    print("5 - Exit")
    choice = -1
    while(choice == -1):
        error = "Valid options are between 1 and 5"
        choice = readInteger("Enter choice: ", error)
        if choice < 1 or choice > 7:
            print(error)
            choice = -1
    print()
    return choice


def main():
    choice = menu()
    while choice != 5:
        if choice == 1:
            size = readInteger("Enter size: ")
            width = readInteger("Enter width: ")
            height = readInteger("Enter height: ")
            repeatingShapes.printCheckerboard(size, width, height)

        elif choice == 2:
            size = readInteger("Enter size: ")
            width = readInteger("Enter width: ")
            height = readInteger("Enter height: ")
            repeatingShapes.printBoxGrid(size, width, height)

        elif choice == 3:
            size = readInteger("Enter size: ")
            width = readInteger("Enter width: ")
            height = readInteger("Enter height: ")
            repeatingShapes.printTrianglePattern(size, width, height)

        elif choice == 4:
            size = readInteger("Enter size: ")
            width = readInteger("Enter width: ")
            height = readInteger("Enter height: ")
            repeatingShapes.printDiamondPattern(size, width, height)

        # read another choice
        choice = menu()


if __name__ == "__main__":
    main()
