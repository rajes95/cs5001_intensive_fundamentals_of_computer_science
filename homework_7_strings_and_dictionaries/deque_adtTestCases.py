# Author: Rajesh Sakhamuru
# Version: 3/28/2019


import unittest
import deque_adt


class Deque_Adt_Test(unittest.TestCase):

    def testAppend(self):
        """
        GIVEN: a List and any object that can be placed into that list
        WHEN: append(value, List) function is called
        THEN: the value should be added to the right side of the list in the
              returned list
        """
        testList = [2, 3, 4]   # TEST CASE 1
        newList = deque_adt.append(1, testList)
        self.assertEqual(newList, [2, 3, 4, 1])
        testList = [2, 3, 4]   # TEST CASE 2
        newList = deque_adt.append(5, testList)
        self.assertEqual(newList, [2, 3, 4, 5])

    def testAppendLeft(self):
        """
        GIVEN: a List and any object that can be placed into that list
        WHEN: appendLeft(value, List) function is called
        THEN: the value should be added to the left side of the list in the
              returned list at index 0
        """
        testList = [2, 3, 4]   # TEST CASE 1
        newList = deque_adt.appendLeft(1, testList)
        self.assertEqual(newList, [1, 2, 3, 4])
        testList = [2, 3, 4]   # TEST CASE 2
        newList = deque_adt.appendLeft(5, testList)
        self.assertEqual(newList, [5, 2, 3, 4])

    def testPop(self):
        """
        GIVEN: a List with 1 or more objects in it
        WHEN: pop(List) function is called
        THEN: the value at the right side (the end) of the list is deleted
        """
        testList = [2, 3, 4]      # TEST CASE 1
        newList = deque_adt.pop(testList)
        self.assertEqual(newList, [2, 3])
        testList = [2, 3, 4, 5]   # TEST CASE 2
        newList = deque_adt.pop(testList)
        self.assertEqual(newList, [2, 3, 4])

    def testPopLeft(self):
        """
        GIVEN: a List with 1 or more objects in it
        WHEN: popLeft(List) function is called
        THEN: the value at the left-most side (the beginning)
              of the list is deleted from index 0
        """
        testList = [2, 3, 4]      # TEST CASE 1
        newList = deque_adt.popLeft(testList)
        self.assertEqual(newList, [3, 4])
        testList = [5, 2, 3, 4]   # TEST CASE 2
        newList = deque_adt.popLeft(testList)
        self.assertEqual(newList, [2, 3, 4])


if __name__ == "__main__":
    unittest.main(exit=False)
