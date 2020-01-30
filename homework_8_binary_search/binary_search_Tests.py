# Author: Rajesh Sakhamuru
# Version: 3/28/2019


import unittest
import binary_search


class Binary_Search_Test(unittest.TestCase):

    def testBinarySearch(self):
        """
        GIVEN: a List of integers and any integer
        WHEN: binary_search(List, Integer) function is called
        THEN: if Integer is in the List, True is returned, otherwise
              False is returned.
        """
        testList = [1, 2, 3]        # TEST CASE 1
        testBool = binary_search.binary_search(testList, 1)
        self.assertEqual(testBool, True)
        testList = [1, 1, 1, 1]     # TEST CASE 2
        testBool = binary_search.binary_search(testList, 2)
        self.assertEqual(testBool, False)
        testList = []               # TEST CASE 3
        testBool = binary_search.binary_search(testList, 0)
        self.assertEqual(testBool, False)
        testList = [0]              # TEST CASE 4
        testBool = binary_search.binary_search(testList, 0)
        self.assertEqual(testBool, True)


if __name__ == "__main__":
    unittest.main(exit=False)
