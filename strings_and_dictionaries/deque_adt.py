# Author: Rajesh Sakhamuru
# Version: 3/28/2019


def append(value, List):
    """
    #### Purpose
    # This function adds a value to the right (or end) of the deque, and returns the deque
    #
    #### Signature
    # append :: (value, List) => List
    #
    #### Examples
    # append(1, [2,3,4]) => [2,3,4,1]
    # append(5, [2,3,4]) => [2,3,4,5]
    """
    List += [value]
    return List


def appendLeft(value, List):
    """
    #### Purpose
    # This function adds a value to the left (or beginning) of the deque, and returns the deque
    #
    #### Signature
    # appendLeft :: (value, List) => List
    #
    #### Examples
    # appendLeft(1, [2,3,4]) => [1,2,3,4]
    # appendLeft(5, [2,3,4]) => [5,2,3,4]
    """
    List = [value] + List
    return List


def pop(List):
    """
    #### Purpose
    # This function removes a value to the right (or end) of the deque, and returns the deque
    #
    #### Signature
    # pop :: List => List
    #
    #### Examples
    # pop([2,3,4]) => [2,3]
    # pop([2,3,4,5]) => [2,3,4]
    """
    newList = []
    for r in range(len(List) - 1):
        newList += [List[r]]
    return newList


def popLeft(List):
    """
    #### Purpose
    # This function removes a value to the left (or beginning) of the deque, and returns the deque
    #
    #### Signature
    # popLeft :: List => List
    #
    #### Examples
    # popLeft([2,3,4]) => [3,4]
    # popLeft([5,2,3,4]) => [2,3,4]
    """
    newList = []
    for r in range(len(List)):
        if r != 0:
            newList += [List[r]]
    return newList
