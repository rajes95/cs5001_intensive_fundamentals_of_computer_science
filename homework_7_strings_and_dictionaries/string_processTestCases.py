# Author: Rajesh Sakhamuru
# Version: 3/26/2019


import unittest
import string_process


class String_Process_Test(unittest.TestCase):

    def testToUpper(self):
        """
        GIVEN: any string object
        WHEN: to_upper(string) function is called with a string parameter
        THEN: all of the lowercase letters in the returned string should be uppercase
              but otherwise identical to the original string
        """
        testString = "test string 9000"   # TEST CASE 1
        capsString = string_process.to_upper(testString)
        self.assertEqual(capsString, "TEST STRING 9000")
        testString = "ThIs Is A sTrInG"   # TEST CASE 2
        capsString = string_process.to_upper(testString)
        self.assertEqual(capsString, "THIS IS A STRING")

    def testToLower(self):
        """
        GIVEN: any string object
        WHEN: to_lower(string) function is called with a string parameter
        THEN: all of the uppercase letters in the returned string should be lowercase
              but otherwise identical to the original string
        """
        testString = "SHOUTY STRING"     # TEST CASE 1
        lowString = string_process.to_lower(testString)
        self.assertEqual(lowString, "shouty string")
        testString = "ThIs Is A sTrInG"  # TEST CASE 2
        lowString = string_process.to_lower(testString)
        self.assertEqual(lowString, "this is a string")

    def testInReverse(self):
        """
        GIVEN: any string object
        WHEN: in_reverse(string) funtion is called with a string parameter
        THEN: characters in the returned string will be in the reverse order
              compared to the original string.
        """
        testString = "Tuesday 3:00 PM"  # TEST CASE 1
        revString = string_process.in_reverse(testString)
        self.assertEqual(revString, "MP 00:3 yadseuT")
        testString = "abcde"            # TEST CASE 2
        revString = string_process.in_reverse(testString)
        self.assertEqual(revString, "edcba")

if __name__ == "__main__":
    unittest.main(exit=False)
