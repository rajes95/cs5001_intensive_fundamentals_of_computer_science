# Author: Rajesh Sakhamuru
# Version: 3/28/2019


def to_upper(string):
    """
    #### Purpose
    # This function takes a string as input and returns the uppercase version of the string
    #
    #### Signature
    # to_upper :: String => String
    #
    #### Template
    # def to_upper(given…):
    #   return returns…
    #
    #### Examples
    # to_upper("test string 9000") => "TEST STRING 9000"
    # to_upper("ThIs Is A sTrInG") => "THIS IS A STRING"
    """
    strList = list(string)
    tempStr = ""
    for n in range(len(strList)):
        if ord(strList[n]) >= 97 and ord(strList[n]) <= 122:
            strList[n] = chr(ord(strList[n]) - 32)
        tempStr += strList[n]
    string = tempStr
    return string


def to_lower(string):
    """
    #### Purpose
    # This function takes a string as input and returns the lowercase version of the string
    #
    #### Signature
    # to_lower :: String => String
    #
    #### Template
    # def to_lower(given…):
    #   return returns...
    #
    #### Examples
    # to_lower("SHOUTY STRING") => "shouty string"
    # to_lower("ThIs Is A sTrInG") => "this is a string"
    """
    strList = list(string)
    tempStr = ""
    for n in range(len(strList)):
        if ord(strList[n]) >= 65 and ord(strList[n]) <= 90:
            strList[n] = chr(ord(strList[n]) + 32)
        tempStr += strList[n]
    string = tempStr
    return string


def in_reverse(string):
    """
    #### Purpose
    # This function takes a string as input and returns the reverse
    of that string, maintaining the case of the original string.
    #
    #### Signature
    # in_reverse :: String => String
    #
    #### Template
    # def in_reverse(given…):
    #   return returns...
    #
    #### Examples
    # in_reverse("Tuesday 3:00 PM") => "MP 00:3 yadseuT"
    # in_reverse(abcde) => "edcba"
    """
    strList = list(string)
    tempStr = ""
    for n in range(-1, -1 * len(strList) - 1, -1):
        tempStr += strList[n]
    string = tempStr
    return string
