# Author: Rajesh Sakhamuru
# Version: 1/20/2019


import unittest
import moreFunctions


class MoreFunctionsTest(unittest.TestCase):

    # Replace "pass" with your test methods
    def testPrintFlag(self):
        """
        GIVEN: --
        WHEN: printFlag() is called
        THEN: a flag is printed to then be visually inspected for accuracy
        """
        moreFunctions.printFlag()

    def testStarWithTwoInts(self):
        """
        GIVEN: To test product of 10 and 5
        WHEN: star(10, 5) is called
        THEN: 50 is returned
        """
        x = moreFunctions.star(10, 5)
        self.assertEqual(x, 50)

    def testStarWithTwoFloats(self):
        """
        GIVEN: To test product of 10 and 5
        WHEN: star(10.3, 5.3) is called
        THEN: 54.59 is returned
        """
        x = moreFunctions.star(10.3, 5.3)
        self.assertEqual(x, 54.59)

    def testStarWithTwoNegFloats(self):
        """
        GIVEN: To test product of -10.4 and -4.7
        WHEN: star(-10.4, -4.7) is called
        THEN: 48.88 is returned
        """
        x = moreFunctions.star(-10.4, -4.7)
        self.assertEqual(x, 48.88)

    def testStarWithIntAndFloat(self):
        """
        GIVEN: To test product of 10 and 4.5
        WHEN: star(10, 4.5) is called
        THEN: 45 is returned
        """
        x = moreFunctions.star(10, 4.5)
        self.assertEqual(x, 45)

    def testStarWithIntAndString(self):
        """
        GIVEN: To test product of 5 and "hi "
        WHEN: star(5, "hi ") is called
        THEN: "hi hi hi hi hi " is returned
        """
        x = moreFunctions.star(5, "hi ")
        self.assertEqual(x, "hi hi hi hi hi ")

    def testStarWithStringAndInt(self):
        """
        GIVEN: To test product of "hi " and 5
        WHEN: star("hi ", 5) is called
        THEN: "hi hi hi hi hi " is returned
        """
        x = moreFunctions.star("hi ", 5)
        self.assertEqual(x, "hi hi hi hi hi ")

    def testStarWithStringAndInt(self):
        """
        GIVEN: To test product of "hi " and 5
        WHEN: star("hi ", 5) is called
        THEN: "hi hi hi hi hi " is returned
        """
        x = moreFunctions.star("hi ", 5)
        self.assertEqual(x, "hi hi hi hi hi ")

    def testReformatNameFirstCaps(self):
        """
        GIVEN: To test reformatting of 'Raj' and 'Sakhamuru'
        WHEN: reformatName('Raj','Sakhamuru') is called
        THEN: "Raj SAKHAMURU" is returned
        """
        x = moreFunctions.reformatName('Raj',  'Sakhamuru')
        self.assertEqual(x, "Raj SAKHAMURU")

    def testReformatNameLwrCase(self):
        """
        GIVEN: To test reformatting of 'raj' and 'sakhamuru'
        WHEN: reformatName('raj','sakhamuru') is called
        THEN: "Raj SAKHAMURU" is returned
        """
        x = moreFunctions.reformatName('raj', 'sakhamuru')
        self.assertEqual(x, "Raj SAKHAMURU")

    def testReformatNameSomeCaps(self):
        """
        GIVEN: To test reformatting of 'RaJ' and 'sakhAmUru'
        WHEN: reformatName('RaJ','sakhAmUru') is called
        THEN: "Raj SAKHAMURU" is returned
        """
        x = moreFunctions.reformatName('RaJ', 'sakhAmUru')
        self.assertEqual(x, "Raj SAKHAMURU")

    def testReformatNameLastLtrCaps(self):
        """
        GIVEN: To test reformatting of 'raJ' and 'sakhamurU'
        WHEN: reformatName('raJ','sakhamurU') is called
        THEN: "Raj SAKHAMURU" is returned
        """
        x = moreFunctions.reformatName('raJ', 'sakhamurU')
        self.assertEqual(x, "Raj SAKHAMURU")

    def testReformatNameOutputAsInput(self):
        """
        GIVEN: To test reformatting of 'Raj' and 'SAKHAMURU'
        WHEN: reformatName('Raj','SAKHAMURU') is called
        THEN: "Raj SAKHAMURU" is returned
        """
        x = moreFunctions.reformatName('Raj', 'SAKHAMURU')
        self.assertEqual(x, "Raj SAKHAMURU")

    def testReformatNameWithNumsAndSpaces(self):
        """
        GIVEN: To test reformatting of '3aj' and ' sak ha m111'
        WHEN: reformatName('3aj',' sak ha m111') is called
        THEN: 3aj  SAK HA M111 is returned
        """
        x = moreFunctions.reformatName('3aj', ' sak ha m111')
        self.assertEqual(x, "3aj  SAK HA M111")

if __name__ == "__main__":
    unittest.main(exit=False)
