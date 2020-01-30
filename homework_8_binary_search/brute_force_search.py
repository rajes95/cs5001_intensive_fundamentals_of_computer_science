# Author:  Rajesh Sakhamuru
# Version: 04-06-2019


def brute_force_search(List, Int):
    """
    # Purpose
    This function takes a List and an Integer as input, and returns
    True if the Integer is in the List and False otherwise.

    # Signature
    brute_force_search :: (List, Integer) => Boolean

    # Example
    brute_force_search :: ([1,2,3], 1) => True
    brute_force_search :: ([1,1,1,1], 2) => False
    """
    for i in range(len(List)):
        if List[i] == Int:
            return True
    return False
