# Author: Rajesh Sakhamuru
# Version: 3/28/2019


import unittest
import binary_search_tree


class Binary_Search_Tree_Tests(unittest.TestCase):

    def testBinarySearchTreeAdd(self):
        """
        # Purpose: This method adds a specified value to the binary tree
                   in the expected location. Lower values are on the left
                   and higher values are on the right. No return value, but
                   the data is stored within the tree.
        # Signature:
                   add :: (self, Integer) => None
        # Examples:
                   add :: (self, 8) => None
                   add :: (self, 5) => None
        """
        testTree = binary_search_tree.BinaryTree(8)
        self.assertEqual(testTree.data, 8)
        testTree.add(3)
        testTree.add(10)
        testTree.add(1)
        testTree.add(6)
        testTree.add(4)
        testTree.add(7)
        testTree.add(14)
        testTree.add(13)
        self.assertEqual(testTree.right.data, 10)      # TEST CASES 1-18
        self.assertEqual(testTree.right.left, None)
        self.assertEqual(testTree.left.data, 3)
        self.assertEqual(testTree.left.left.data, 1)
        self.assertEqual(testTree.left.left.left, None)
        self.assertEqual(testTree.left.left.right, None)
        self.assertEqual(testTree.left.right.data, 6)
        self.assertEqual(testTree.left.right.left.data, 4)
        self.assertEqual(testTree.left.right.left.left, None)
        self.assertEqual(testTree.left.right.left.right, None)
        self.assertEqual(testTree.left.right.right.data, 7)
        self.assertEqual(testTree.left.right.right.left, None)
        self.assertEqual(testTree.left.right.right.right, None)
        self.assertEqual(testTree.right.right.data, 14)
        self.assertEqual(testTree.right.right.left.data, 13)
        self.assertEqual(testTree.right.right.left.right, None)
        self.assertEqual(testTree.right.right.left.left, None)
        self.assertEqual(testTree.right.right.right, None)

    def testBinarySearchTreeGet(self):
        """
        # Purpose: This method searches the binary tree for a specified
                   value (num) and if that value is in the tree, then num is
                   returned and if it is not, then None is returened.
        # Signature:
                   get :: (self, Integer) => Integer (or none)
        # Examples:
                   get :: (self, 5) => 5     # if 5 is in the Tree
                   get :: (self, 8) => None  # if 8 is not in the Tree
        """
        testTree = binary_search_tree.BinaryTree(8)
        self.assertEqual(testTree.data, 8)
        testTree.add(3)
        testTree.add(10)
        testTree.add(1)
        testTree.add(6)
        getData = testTree.get(3)       # TEST CASE 1
        self.assertEqual(getData, 3)
        getData = testTree.get(8)       # TEST CASE 2
        self.assertEqual(getData, 8)
        getData = testTree.get(10)      # TEST CASE 3
        self.assertEqual(getData, 10)
        getData = testTree.get(1)       # TEST CASE 4
        self.assertEqual(getData, 1)
        getData = testTree.get(6)       # TEST CASE 5
        self.assertEqual(getData, 6)
        getData = testTree.get(5)       # TEST CASE 6
        self.assertEqual(getData, None)
        getData = testTree.get(0)       # TEST CASE 7
        self.assertEqual(getData, None)
        getData = testTree.get(-7)      # TEST CASE 8
        self.assertEqual(getData, None)

if __name__ == "__main__":
    unittest.main(exit=False)
