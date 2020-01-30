# Author: Rajesh Sakhamuru
# Version: 2/4/2019


import unittest
import moreSelection


class MoreSelectionTests(unittest.TestCase):

    # Replace "pass" with your test methods
    def testLargest1(self):
        """
        GIVEN: parameters of -2, -1, 0, 1, 2
        WHEN: largest(-2, -1, 0, 1, 2) is called
        THEN: 2 is returned
        """
        x = moreSelection.largest(-2, -1, 0, 1, 2)
        self.assertEqual(x, 2)

    def testLargest2(self):
        """
        GIVEN: parameters of -5, -4, -3, -2, -1
        WHEN: largest(-5, -4, -3, -2, -1) is called
        THEN: -1 is returned
        """
        x = moreSelection.largest(-5, -4, -3, -2, -1)
        self.assertEqual(x, -1)

    def testLargest3(self):
        """
        GIVEN: parameters of 5.5, 4.5, 3.5, 2.5, 1.5
        WHEN: largest(5.5, 4.5, 3.5, 2.5, 1.5) is called
        THEN: 5.5 is returned
        """
        x = moreSelection.largest(5.5, 4.5, 3.5, 2.5, 1.5)
        self.assertEqual(x, 5.5)

    def testLargest4(self):
        """
        GIVEN: parameters of 1, 1.0, 1, 1.0, 1
        WHEN: largest(1, 1.0, 1, 1.0, 1) is called
        THEN: 1 is returned
        """
        x = moreSelection.largest(1, 1.0, 1, 1.0, 1)
        self.assertEqual(x, 1.0)

    def testLargest5(self):
        """
        GIVEN: parameters of -5.5, -4.5, -3.5, -2.5, -1.5
        WHEN: largest(-5.5, -4.5, -3.5, -2.5, -1.5) is called
        THEN: -1.5 is returned
        """
        x = moreSelection.largest(-5.5, -4.5, -3.5, -2.5, -1.5)
        self.assertEqual(x, -1.5)

    def testLargest6(self):
        """
        GIVEN: parameters of -2.5, -1.5, 0.5, 1.5, 2.5
        WHEN: largest(-2.5, -1.5, 0.5, 1.5, 2.5) is called
        THEN: 2.5 is returned
        """
        x = moreSelection.largest(-2.5, -1.5, 0.5, 1.5, 2.5)
        self.assertEqual(x, 2.5)

    def testChangeMaker1(self):
        """
        GIVEN: parameters of 13.57 owed, 100 paid
        WHEN: changeMaker(13.57, 100) is called
        THEN: 'Change: $86.43\n4 twenties\n1 five\n1 one\n1 quarter\n1 dime\n1 nickel\n3 pennies'
              is returned with '\n' in the string indicating a new line
        """
        x = moreSelection.changeMaker(13.57, 100)
        self.assertEqual(x, 'Change: $86.43\n4 twenties\n1 five\n1 one\n1 quarter\n1 dime\n1 nickel\n3 pennies')

    def testChangeMaker2(self):
        """
        GIVEN: parameters of 40.66 owed, 77.07 paid
        WHEN: changeMaker(40.66, 77.07) is called
        THEN: 'Change: $36.41\n1 twenty\n1 ten\n1 five\n1 one\n1 quarter\n1 dime\n1 nickel\n1 penny'
              is returned with '\n' in the string indicating a new line
        """
        x = moreSelection.changeMaker(40.66, 77.07)
        self.assertEqual(x, 'Change: $36.41\n1 twenty\n1 ten\n1 five\n1 one\n1 quarter\n1 dime\n1 nickel\n1 penny')

    def testChangeMaker3(self):
        """
        GIVEN: parameters of 10.01 owed, 68.95 paid
        WHEN: changeMaker(10.01, 68.95) is called
        THEN: 'Change: $58.94\n2 twenties\n1 ten\n1 five\n3 ones\n3 quarters\n1 dime\n1 nickel\n4 pennies'
              is returned with '\n' in the string indicating a new line
        """
        x = moreSelection.changeMaker(10.01, 68.95)
        expected = 'Change: $58.94\n2 twenties\n1 ten\n1 five\n3 ones\n3 quarters\n1 dime\n1 nickel\n4 pennies'
        self.assertEqual(x, expected)

    def testChangeMaker4(self):
        """
        GIVEN: parameters of 0 owed, 0 paid
        WHEN: changeMaker(0, 0) is called
        THEN: 'Change: $0.00' is returned
        """
        x = moreSelection.changeMaker(0, 0)
        self.assertEqual(x, 'Change: $0.00')

    def testChangeMaker5(self):
        """
        GIVEN: parameters of 20.20 owed, 20.20 paid
        WHEN: changeMaker(20.20, 20.20) is called
        THEN: 'Change: $0.00' is returned
        """
        x = moreSelection.changeMaker(20.20, 20.20)
        self.assertEqual(x, 'Change: $0.00')

    def testChangeMaker6(self):
        """
        GIVEN: parameters of 36.80 owed, 50 paid
        WHEN: changeMaker(36.80, 50) is called
        THEN: 'Change: $13.20\n1 ten\n3 ones\n2 dimes'
              is returned with '\n' in the string indicating a new line
        """
        x = moreSelection.changeMaker(36.80, 50)
        self.assertEqual(x, 'Change: $13.20\n1 ten\n3 ones\n2 dimes')

    def testMultiply1(self):
        """
        GIVEN: parameters of 5, 6
        WHEN: multiply(5, 6) is called
        THEN: 30 is returned
        """
        x = moreSelection.multiply(5, 6)
        self.assertEqual(x, 30)

    def testMultiply2(self):
        """
        GIVEN: parameters of 5.0, 6.0
        WHEN: multiply(5.0, 6.0) is called
        THEN: 30.0 is returned
        """
        x = moreSelection.multiply(5.0, 6.0)
        self.assertEqual(x, 30.0)

    def testMultiply3(self):
        """
        GIVEN: parameters of -5, 6
        WHEN: multiply(-5, 6) is called
        THEN: -30 is returned
        """
        x = moreSelection.multiply(-5, 6)
        self.assertEqual(x, -30)

    def testMultiply4(self):
        """
        GIVEN: parameters of -5.0, 6.0
        WHEN: multiply(-5.0, 6.0) is called
        THEN: -30.0 is returned
        """
        x = moreSelection.multiply(-5.0, 6.0)
        self.assertEqual(x, -30.0)

    def testMultiply5(self):
        """
        GIVEN: parameters of 6, -5
        WHEN: multiply(6, -5) is called
        THEN: 0 is returned
        """
        x = moreSelection.multiply(6, -5)
        self.assertEqual(x, 0)

    def testMultiply6(self):
        """
        GIVEN: parameters of 0, 0
        WHEN: multiply(0, 0) is called
        THEN: 0 is returned
        """
        x = moreSelection.multiply(0, 0)
        self.assertEqual(x, 0)


if __name__ == "__main__":
    unittest.main(exit=False)
