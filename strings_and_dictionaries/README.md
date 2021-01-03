**CS5001** Silicon Valley

**Spring 2019**

**HW7 (Strings and Dictionaries)**

**Assigned:** March 21, 2019

**Deadline:** March 28, 2019 11:59pm

Your solution will be evaluated according to the following [grading rubric](https://s3.us-east-1.amazonaws.com/blackboard.learn.xythos.prod/5a3148150d016/15626539?response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27Spring%25202019%2520CS5001%2520Silicon%2520Valley.pdf&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20190320T155748Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=AKIAIL7WQYDOOHAZJGWQ%2F20190320%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a486a62123a713598dc1b4677c00684f5327bdd765f943b5ce2fc6c3354198d9). Normally, the written component accounts for 30% of your overall HW1 score; the programming component for 70%. For this assignment, however, grading will be lenient.  Familiarize yourself with the rubric, as it will be used for all subsequent assignments.

Your completed work should be compressed and submitted to Bottlenose following this naming convention: `firstName_lastName_assignment7.zip` for the normal questions, and `firstName_lastName_extraCredit7.zip` for the extra credit.

#### Written Component

Please open a plaintext file (you can do this in any plaintext editor you like, such as TextEdit or NotePad) and type out your answers to the questions below. You can type your answers into Python to confirm, but try answering the questions first.

##### Written #1

Describe the following operations in the `List` ADT: `get`, `insert`, `remove`, and `size`.



##### Written #2

Assume the following definitions and operations:

```python
names = ["Drew", "Yi", "Tian", "Lucas"]

new_names = [name.lower() for name in names]

def filter_names(name):
    return len(name) <= 2

filtered_names = list(filter(filter_names, new_names))
```

Describe what each line of code does.



##### Written #3 (Extra Credit, 5%)

Assume the following definitions and operations:

```python
names = ["Drew", "Yi", "Tian", "Lucas"]

below_two = reduce(lambda acc, cur: len(cur) > 2 and acc, names, True)

assert(not below_two)
```

I only mentioned `reduce` during lecture and did not mention `lambda`.  For extra credit, describe what each line of code does.

**Programming Component**

**Code Structure and Style**

Follow the PEP 8 style guide.  _Tip: Use the design recipe to write and document your functions._ Some reminders:

- Place each of the following programs in their own file
- Make sure that your functions are modular—one action per function
- Avoid “magic numbers” by using constants where appropriate
- Write Pytest test cases for every function (except main()). Write as many test cases as you need to feel confident that your code works as expected. We expect to see test cases even if the problem text doesn’t explicitly mention test cases.



##### Programming #1

- Filename: string_process.py

You've used Python’s built-in string methods upper() and lower() to change the case of a string. In this problem, you’re going to write three functions of your own to process strings without using any of Python’s built-in string methods (.upper(), .lower(), or anything else written with dot notation). In your Python file, do the following:

- Write a function that takes a string as input and returns the uppercase version of that string.
- Write a function that takes a string as input and returns the lowercase version of that string.
- Write a function that takes a string as input and returns the reverse of that string. 

Use the three design recipes below to write your functions:

```python
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
# to_upper(“test string 9000”) => “TEST STRING 9000”
# to_upper(“ThIs Is A sTrInG”) => “THIS IS A STRING”


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
# to_lower(“SHOUTY STRING”) => “shouty string”
# to_lower(“ThIs Is A sTrInG”) => “this is a string”


#### Purpose
# This function takes a string as input and returns the reverse of that string, maintaining the case of the original string.
#
#### Signature
# in_reverse :: String => String
#
#### Template
# def in_reverse(given…):
#   return returns...
#
#### Examples
# in_reverse(“Tuesday 3:00 PM”) => “MP 00:3 yadseuT”
# in_reverse(“abcde”) => “edcba”
```

*Helpful hint:*

- Strings can be traversed similar to Lists (iteration)

###### Requirements

- Write three separate functions following the given Design Recipes
- Do not use Python’s built-in string methods i.e. .upper(), .lower(), or anything else written with dot notation.
- Each function should include __at least__ two test cases



##### Programming #2

- Filename: deque_adt.py

During a lecture exercise, we implemented the `push`, `pop`, `peek`, and `size` operations of the `Stack` ADT.  A Double-ended Queue, or`deque`, is a data structure which allows `enqueing` from both sides of the structure.  More can be read [here](https://en.wikipedia.org/wiki/Double-ended_queue).

Implement the following `deque` operations: `append`, `appendLeft`, `pop`, `popleft`.

Use the five design recipes below to write your functions:

```python
#### Purpose
# This function adds a value to the right (or end) of the deque, and returns the deque
#
#### Signature
# append :: (value, List) => List
#
#### Examples
# append(1, [2,3,4]) => [2,3,4,1]
# append(5, [2,3,4]) => [2,3,4,5]

#### Purpose
# This function adds a value to the left (or beginning) of the deque, and returns the deque
#
#### Signature
# appendLeft :: (value, List) => List
#
#### Examples
# appendLeft(1, [2,3,4]) => [1,2,3,4]
# appendLeft(5, [2,3,4]) => [5,2,3,4]

#### Purpose
# This function removes a value to the right (or end) of the deque, and returns the deque
#
#### Signature
# pop :: List => List
#
#### Examples
# pop([2,3,4]) => [2,3]
# pop([2,3,4,5]) => [2,3,4]

#### Purpose
# This function removes a value to the left (or beginning) of the deque, and returns the deque
#
#### Signature
# popLeft :: List => List
#
#### Examples
# popLeft([2,3,4]) => [3,4]
# popLeft([5,2,3,4]) => [2,3,4]
```

_Helpful Hint_

- Remember, we're implementing the behavior of the `Deque` by using a `List`. Refer back to the lecture notes for reference (`Stack` exercise).

  

###### Requirements

- Each function should follow the signature specified in the provided Design Recipe
- Each function should include __at least__ 2 test cases

##### Programming #3

- Filename: upc.py

The modulo operator, %,  can be useful in surprising ways -- like making sure we don’t accidentally overpay at a checkout register. Every item you purchase has a Universal Product Code (UPC), which you’ll see on a sticker or otherwise attached to it, along with a barcode used for scanning. Like this:

![img](https://lh5.googleusercontent.com/-LgbTmhh6j8BUsamu87QrB3bJ6cEtY8QpsTFohRNJuuZASmFduRH0Q0UWBX-uOvk1Q0C6HkY8r4f_JkNJAdvEuhnA-kuKxtRZb3ELOquOi6cYJbLYPMFJpL07mvcY7kw2iG_SyUc)

Most of these digits are chosen to specify the manufacturer, product type, country, etc., but one of them is set aside to be the “check digit.” After all the other numbers are set, the check digit is chosen such that a calculation we apply to the numbers will end up being a multiple of 10.

Why are UPC codes designed this way? Because, if you’re typing one up on a cash register or in a database for an online store, if you make a mistake... it’s super easy to tell. 

For UPC numbers, the validation algorithm proceeds on the number **from right to left:**

- Digits in even positions, including zero: no change
- Digits in odd positions: *3
- Sum the results

If it’s a valid UPC number, this result is a multiple of 10.

The UPC number above is `0 7 3 8 5 4 0 0 8 0 8 9`.

We apply the algorithm (the number above is written from left to right, but the algorithm goes right to left, so we say 9 is at position 0, 8 is at position 1, etc.):  

```bash
9 + (8 * 3) + 0 + (8 * 3) + 0 + (0 * 3) + 4 + (5 * 3) + 8 + (3 * 3) + 7 + (0 * 3)

​	= 9 + 24 + 0 + 24 + 0 + 0 + 4 + 15 + 8 + 9 + 7 + 0

​	= 100
```

And we’re done! We’ve verified that this, in fact, a valid UPC number.

For this assignment, write a Python program that prompts the user to enter a UPC code. UPC codes can be different lengths, so don’t assume it’ll always be exactly 12 digits.  The program should return either 1 of two results: `Valid UPC` or `Not a valid UPC`.

###### Requirements:

- Your program should expect a String as input

- Your program should `print` the response to console

- Your program must include at least 3 test cases

  

##### Programming #4 (Extra Credit, 5%)

- Filename: extra.py

User input is a common way for program to interact with users.  Explore Python's features for user input.  The documentation can be found [here]().

Using a __complete__ Design Recipe, design a program which prompts the user for the current date and returns the number of days between the current date and the New Year.

###### Requirements:

- The Design Recipe must be used for __each__ function you define
- The program must prompt the user for input and use that input to calculate the response
- The program must consider edge cases (Leap Year, for example)
- Your program only needs to support a single input date format, but that format must be clearly outlined in your Design Recipe
- Your program only needs to support a single response format, but that format must be clearly outlined in your Design Recipe
- Your program should `print` the response to console
- Your program must be __well__ tested


