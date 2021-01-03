# Author:  Rajesh Sakhamuru
# Version: 04-06-2019


def binary_search(List, Int):
    """
    # Purpose
    This function takes a List and an Integer as input, and returns True if the
    Integer is in the List and False otherwise.

    # Signature
    binary_search :: (List, Integer) => Boolean

    # Example
    binary_search :: ([1,2,3], 1) => True
    binary_search :: ([1,1,1,1], 2) => False
    """
    found = False
    if len(List) == 0:
        return found
    start = 0
    end = len(List) - 1
    mid = round((start + end) / 2)
    counter = 0
    if List[start] == Int or List[end] == Int or List[mid] == Int:
        return True
    while found is False:
        if Int > List[mid]:
            start = mid
        elif Int < List[mid]:
            end = mid
        mid = round((start + end) / 2)
        if List[mid] == Int:
            found = True
        counter += 1
        if counter >= len(List):
            break
    return found
