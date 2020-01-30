# Author: Rajesh Sakhamuru
# Version: 3/26/2019


import unittest
import upc


class UPCTest(unittest.TestCase):

    def testUpcCodeScanner(self):
        """
        GIVEN: a UPC code as a string
        WHEN: upcCodeScanner(UPC) function is called
        THEN: the validity of the UPC code is determined and either
              'Valid UPC' or 'Not a valid UPC' is returned.
        """
        testUPC = "073854008089"        # TEST CASE 1
        validity = upc.upcCodeScanner(testUPC)
        self.assertEqual(validity, "Valid UPC")
        testUPC = "93854008089"         # TEST CASE 2
        validity = upc.upcCodeScanner(testUPC)
        self.assertEqual(validity, "Not a valid UPC")
        testUPC = "042100005264"         # TEST CASE 3
        validity = upc.upcCodeScanner(testUPC)
        self.assertEqual(validity, "Valid UPC")

    def testUpcCodeScannerUserInput(self):
        """
        GIVEN: a UPC code as a string
        WHEN: upcCodeScanner() function is called and the UPC code can be
              entered by the user
        THEN: the validity of the UPC code is determined and either
              'Valid UPC' or 'Not a valid UPC' is printed.
              Whether the program works correctly should be determined by the
              person testing.
        """
        print()
        upc.upcCodeScanner()    # TEST CASE 4
        # Should take user input of UPC input of 042100005264 should
        # result in output print statement of "Valid UPC"

if __name__ == "__main__":
    unittest.main(exit=False)
