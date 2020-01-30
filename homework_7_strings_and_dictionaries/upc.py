# Author: Rajesh Sakhamuru
# Version: 3/26/2019


def upcCodeScanner(upcList=None):
    """
    Purpose
      This function either revieves input as a string parameter or through user
      input of a UPC code. The code is then tested to see if it is valid or not
      and statement of validity is printed.
      For testing purposes, the input (UPC code) can optionally be given as a string
      parameter and the statement of validity is returned by the function.

    Signature
      upcCodeScanner :: upcList = None => "Valid UPC" or "Not a valid UPC"

    Examples
      upcCodeScanner("073854008089") => 'Valid UPC'
      upcCodeScanner("93854008089") => 'Not a valid UPC'
      TEST CASES ARE IN upcTestCases.py
    """
    if upcList is None:
        upcList = list(input("Please enter a UPC code: "))
    else:
        upcList = list(str(upcList))
    sum = 0
    for i in range(-1, -1 * len(upcList) - 1, -1):
        if i % 2 == 0:
            sum += int(upcList[i]) * 3
        else:
            sum += int(upcList[i])
    if sum % 10 == 0:
        print("Valid UPC")
        return "Valid UPC"
    else:
        print("Not a valid UPC")
        return "Not a valid UPC"
