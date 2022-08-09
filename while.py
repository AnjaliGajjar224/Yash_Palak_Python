"""
Loops:
    - While
    - For
"""

"""
Syntax:
-----------------
initialization
while condition:
    statements
    increment/decrement
"""

# i = 1       # initialization

# while i <= 5:         # condition
#     print("Hello")
#     i += 1          # increment/decrement (i += 1---> i = i + 1)

"""
Task 1: Print all the numbers from 1 to n(user input)

    e.g. n = 5
         1 2 3 4 5                 

Task 2: Print all the numbers from n to 1(user input)

    e.g. n = 5
            5 4 3 2 1

Task 3: Find the sum of all the numbers from 1 to n(user input)

Task 4: Find the Factorial of n(user input)
        e.g.

        n = 5
        5 * 4 * 3 * 2 * 1 = 120 = 5!

Task 5: Check whether the number is Palindrom or not.
        e.g.
        1) String:
            "madam" , "racecar" , "radar" , "pop"

        2) Number:  
            12321 , 1234321  , 121 , 212

Task 6: Check whether the number is Armstrong or not.
        e.g.

        153 = 1*1*1 + 5*5*5 + 3*3*3 = 1 + 125 + 27 = 153
        407 , 370 , 371 , 1634 , 8208 , 9474

Task 7: Fibonacci series
        e.g.
        0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

Task 8: Check whether the number is Prime or not.
# """
# n = int(input("Enter the number: "))

# i = n

# while i >= 1:
#     print(i,end=" ")
#     i -= 1

"""
Nested While Loop:
    - While loop inside another while loop

Syntax:
-----------------
initialization
while condition:
    initialization
    while condition:
        statements
        incremenrt/decrement
    increment/decrement
"""
# i = 1

# while i <= 5:
#     j = 1
#     while j <= 5:
#         print("*",end=" ")
#         j += 1
#     print()
#     i += 1

"""
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
# """
# i = 1
# num = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print(num,end=" ")
#         num += 1
#         j += 1
#     print()
#     i += 1

"""
*
* *
* * *
* * * *
* * * * *

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5   

1
1 2 
1 2 3
1 2 3 4
1 2 3 4 5

1
2 3 
4 5 6
7 8 9 10
11 12 13 14

5 
5 4 
5 4 3
5 4 3 2
5 4 3 2 1
# """
# i = 5

# while i >= 1:
#     j = 5
#     while j >= i:
#         print(j,end=" ")
#         j -= 1
#     print()
#     i -= 1

"""
5 4 3 2 1
4 3 2 1 
3 2 1
2 1
1
"""
# n = int(input("Enter a number of rows: "))

# i = 5

# while i >= 1:
#     j = i
#     while j >= 1:
#         print(j,end=" ")
#         j -= 1
#     print()
#     i -= 1

"""
A
B B
C C C
D D D D
E E E E E
"""