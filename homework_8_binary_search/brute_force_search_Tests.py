# Author: Rajesh Sakhamuru
# Version: 3/28/2019


import unittest
import brute_force_search


class Brute_Force_Search_Test(unittest.TestCase):

    def testBruteForceSearch(self):
        """
        GIVEN: a List of integers and any integer
        WHEN: brute_force_search(List, Integer) function is called
        THEN: if Integer is in the List, True is returned, otherwise
              False is returned.
        """
        testList = [1, 2, 3]        # TEST CASE 1
        testBool = brute_force_search.brute_force_search(testList, 1)
        self.assertEqual(testBool, True)
        testList = [1, 1, 1, 1]     # TEST CASE 2
        testBool = brute_force_search.brute_force_search(testList, 2)
        self.assertEqual(testBool, False)
        testList = []               # TEST CASE 3
        testBool = brute_force_search.brute_force_search(testList, 0)
        self.assertEqual(testBool, False)
        testList = [0]               # TEST CASE 4
        testBool = brute_force_search.brute_force_search(testList, 0)
        self.assertEqual(testBool, True)


if __name__ == "__main__":
    unittest.main(exit=False)
