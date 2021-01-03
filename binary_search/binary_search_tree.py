# Author:  Rajesh Sakhamuru
# Version: 04-06-2019


class BinaryTree():
    def __init__(self, value):
        """
        # Purpose: This method is to initialize the BinaryTree class to have a
                   left, right and data value. it sets data of the object equal to
                   a value given in the parameter. No return value.
        # Signature:
                   self.__init__ :: (self, Integer) => None
        # Examples:
                   __init__ :: (self, 5) => None
                   __init__ :: (self, 8) => None
        """
        self.left = None
        self.right = None
        self.data = value

    def add(self, value):
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
        if self.data is None:
            self.data = value
        elif value <= self.data:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.add(value)
        elif value > self.data:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.add(value)

    def get(self, num):
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
        if self.data == num:
            return num
        elif num > self.data:
            if self.right is not None:
                return self.right.get(num)
            else:
                return None
        elif num < self.data:
            if self.left is not None:
                return self.left.get(num)
            else:
                return None
