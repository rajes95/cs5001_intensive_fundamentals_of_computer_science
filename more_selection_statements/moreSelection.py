# Author: Rajesh Sakhamuru
# Version: 2/4/2019


def largest(a, b, c, d, e):
    """
    GIVEN: a, b, c, d, and e as numeric (float or int) values
    WHEN: largest(a, b, c, d, e) is called
    THEN: the function largest() finds which value is largest and returns it
    """
    top = a
    if b > top:
        top = b
    if c > top:
        top = c
    if d > top:
        top = d
    if e > top:
        top = e
    return top


def changeMaker(saleAmount, amountPaid):
    """
    GIVEN: saleAmount and amountPaid as numeric (float or int) values
    WHEN: changeMaker(saleAmount, amountPaid) is called
    THEN: the function changeMaker() subtracts saleAmount from amountPaid
          and determines the amount of change needed to return in twenty, ten,
          five, and one dollar bills, and quarters, dimes, nickels and
          pennies. If that particular denomination is not needed to make change,
          then it is not included in the printed statement.
    """
    totalChange = round(amountPaid - saleAmount, 2)
    twenties = int(totalChange // 20)
    remainingChange = totalChange % 20
    tens = int(remainingChange // 10)
    remainingChange %= 10
    fives = int(remainingChange // 5)
    remainingChange %= 5
    ones = int(remainingChange // 1)
    remainingChange %= 1
    quarters = int(remainingChange // .25)
    remainingChange %= .25
    remainingChange = round(remainingChange * 100, 3)
    dimes = int(remainingChange // 10)
    remainingChange %= 10
    nickels = int(remainingChange // 5)
    remainingChange %= 5
    pennies = int(remainingChange // 1)
    returnString = twentyStr = tenStr = fiveStr = oneStr = quarterStr = dimeStr = nickelStr = pennyStr = ""
    if twenties == 1:
        twentyStr = "twenty"
        returnString += "\n" + str(twenties) + " " + twentyStr
    elif twenties != 0:
        twentyStr = "twenties"
        returnString += "\n" + str(twenties) + " " + twentyStr
    if tens == 1:
        tenStr = "ten"
        returnString += "\n" + str(tens) + " " + tenStr
    elif tens != 0:
        tenStr = "tens"
        returnString += "\n" + str(tens) + " " + tenStr
    if fives == 1:
        fiveStr = "five"
        returnString += "\n" + str(fives) + " " + fiveStr
    elif fives != 0:
        fiveStr = "fives"
        returnString += "\n" + str(fives) + " " + fiveStr
    if ones == 1:
        oneStr = "one"
        returnString += "\n" + str(ones) + " " + oneStr
    elif ones != 0:
        oneStr = "ones"
        returnString += "\n" + str(ones) + " " + oneStr
    if quarters == 1:
        quarterStr = "quarter"
        returnString += "\n" + str(quarters) + " " + quarterStr
    elif quarters != 0:
        quarterStr = "quarters"
        returnString += "\n" + str(quarters) + " " + quarterStr
    if dimes == 1:
        dimeStr = "dime"
        returnString += "\n" + str(dimes) + " " + dimeStr
    elif dimes != 0:
        dimeStr = "dimes"
        returnString += "\n" + str(dimes) + " " + dimeStr
    if nickels == 1:
        nickelStr = "nickel"
        returnString += "\n" + str(nickels) + " " + nickelStr
    elif nickels != 0:
        nickelStr = "nickels"
        returnString += "\n" + str(nickels) + " " + nickelStr
    if pennies == 1:
        pennyStr = "penny"
        returnString += "\n" + str(pennies) + " " + pennyStr
    elif pennies != 0:
        pennyStr = "pennies"
        returnString += "\n" + str(pennies) + " " + pennyStr
    returnString = "Change: $" + '{0:.2f}'.format(totalChange) + returnString
    return returnString


def multiply(x, y):
    """
    GIVEN: x and y as numeric (float or int) values. Function works best with
           positive integer (or 0) input for y.
    WHEN: multiply(x, y) is called
    THEN: the function multiply() recursively calculates the product of x and y.
          This is not the most accurate way of calculating the product, so the
          answer will not always be the actual product. Especially with float
          inputs and negative values. Most accurate using input integers for y
          greater than or equal to 0.
    """
    if y <= 0:
        return 0
    elif y == 1:
        return x
    return (x + multiply(x, y - 1))
