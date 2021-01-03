# Author: Rajesh Sakhamuru
# Version: 1/26/2019


import unittest
import predicateFunctions


class PredicateFunctionsTest(unittest.TestCase):

    # Replace "pass" with your test methods
    def testxorWithTrueTrue(self):
        """
        GIVEN: x == True and y == True
        WHEN: xor(True, True) is called
        THEN: False is returned
        """
        x = predicateFunctions.xor(True, True)
        self.assertFalse(x, msg=None)

    def testxorWithTrueFalse(self):
        """
        GIVEN: x == True and y == False
        WHEN: xor(True, False) is called
        THEN: True is returned
        """
        x = predicateFunctions.xor(True, False)
        self.assertTrue(x, msg=None)

    def testxorWithFalseTrue(self):
        """
        GIVEN: x == False and y == True
        WHEN: xor(False, True) is called
        THEN: True is returned
        """
        x = predicateFunctions.xor(False, True)
        self.assertTrue(x, msg=None)

    def testxorWithFalseFalse(self):
        """
        GIVEN: x == False and y == False
        WHEN: xor(False, False) is called
        THEN: False is returned
        """
        x = predicateFunctions.xor(False, False)
        self.assertFalse(x, msg=None)

    def testisNegativePosInt(self):
        """
        GIVEN: parameter of 10
        WHEN: isNegative(10) is called
        THEN: False is returned
        """
        x = predicateFunctions.isNegative(10)
        self.assertFalse(x, msg=None)

    def testisNegativePosFloat(self):
        """
        GIVEN: parameter of 10.5
        WHEN: isNegative(10.5) is called
        THEN: False is returned
        """
        x = predicateFunctions.isNegative(10.5)
        self.assertFalse(x, msg=None)

    def testisNegativeZero(self):
        """
        GIVEN: parameter of 0
        WHEN: isNegative(0) is called
        THEN: False is returned
        """
        x = predicateFunctions.isNegative(0)
        self.assertFalse(x, msg=None)

    def testisNegativeNegFloat(self):
        """
        GIVEN: parameter of -10.5
        WHEN: isNegative(-10.5) is called
        THEN: True is returned
        """
        x = predicateFunctions.isNegative(-10.5)
        self.assertTrue(x, msg=None)

    def testisNegativeNegInt(self):
        """
        GIVEN: parameter of -10
        WHEN: isNegative(-10) is called
        THEN: True is returned
        """
        x = predicateFunctions.isNegative(-10)
        self.assertTrue(x, msg=None)

    def testisLeapYearMillenium(self):
        """
        GIVEN: year == 2000
        WHEN: isLeapYear(2000) is called
        THEN: True is returned
        """
        x = predicateFunctions.isLeapYear(2000)
        self.assertTrue(x, msg=None)

    def testisLeapYearDivisibleBy4(self):
        """
        GIVEN: year == 2012
        WHEN: isLeapYear(2012) is called
        THEN: True is returned
        """
        x = predicateFunctions.isLeapYear(2012)
        self.assertTrue(x, msg=None)

    def testisLeapYearNonLeapYear(self):
        """
        GIVEN: year == 2018
        WHEN: isLeapYear(2018) is called
        THEN: False is returned
        """
        x = predicateFunctions.isLeapYear(2018)
        self.assertFalse(x, msg=None)

    def testisLeapYearCenturyNonLeapYear(self):
        """
        GIVEN: year == 2100
        WHEN: isLeapYear(2100) is called
        THEN: False is returned
        """
        x = predicateFunctions.isLeapYear(2100)
        self.assertFalse(x, msg=None)


if __name__ == "__main__":
    unittest.main(exit=False)
