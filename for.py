"""
Syntax:
---------
1) for var_name in iterable_object:
         statements

2) for var_name in range(start, end, step):
            statements

"""

# for i in range(5):             # i = 0 (by default) to 4(5 is not included)
#     print("Hello")

# for i in range(5):
    # print(i)

# for i in range(1,5):            # i = 1 to 4 (5 is not included)
#     print(i)

# for i in range(11,21):          # i = 1 to 20 (21 is not included)
#     print(i)

# for i in range(1,10,1):           # i = 1 to 9 (10 is not included) with step 1
#     print(i)

# for i in range(1,10,2):           # i = 1 to 9 (10 is not included) with step 2
#     print(i)

# for i in range(5,0,-1):              # i = 5 to 1 (0 is not included) with step -1
#     print(i)

# for i in range(10,0,-2):
#     print(i)

"""
1. Take two numbers from user and print all the numbers between them.
2. n = 5   O/P : e.g. 1 2 3 4 5
3. n = 5   O/P : e.g. 5 4 3 2 1
"""
"""
1. Take a number from the user and print the table of that number.
2. Factorial of a number is the product of all the numbers from 1 to n.
3. Fibonacci series is a series of numbers in which each number is the sum of previous two numbers.
4. take n from the user and print all the odd numbers ans find sum of the even numbers.
5. Check whether the given number is prime or not.
"""

"""
1. Take starting and ending range from the user and print all the Armstrong numbers between them.
2. Take a range from the user and print all the Prime numbers between them.
3. Take a range from the user and print all the Palindrome numbers between them.
4. Take a range from the user and print all the Twin numbers between them.
e. g. n = 123
        sum = 1 + 2 + 3 = 6
        multiply = 1 * 2 * 3 = 6

        if sum == multiply:
            Twin Number
"""

# start = int(input("Enter starting range: "))
# end = int(input("Enter ending range: "))

# print("Armstrong Numbers: ")
# for i in range(start, end+1):
#     sum = 0
#     temp = i
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** len(str(i))
#         temp //= 10
#     if i == sum:
#         print(i,end=" ")


# Prime numbers

# start = int(input("Enter starting range: "))
# end = int(input("Enter ending range: "))

# print("Prime Numbers: ")
# for num in range(start,end+1):
#     count = 0
#     i = 1
#     while i <= num:
#         if num % i == 0:
#             count += 1
#         i += 1
#     if count == 2:
#         print(num,end=" ")

# Twin numbers

# start = int(input("Enter starting range: "))
# end = int(input("Enter ending range: "))

# print("Twin Numbers: ")
# for num in range(start, end+1):
#     sum = 0
#     mul = 1
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit
#         mul *= digit
#         temp //= 10
#     if sum == mul:
#         print(num,end=" ")

"""
Nested For Loop:
-----------------------

Syntax:
-------------------------

for i in range(start,end, step):
    for j in range(start,end,step):
        statements
    statements

"""

"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()

"""
0 1 0 1 0 
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0 
0 1 0 1 0

0 0 0 0 0 
1 1 1 1 1 
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0

A A A A A
B B B B B
C C C C C
D D D D D
E E E E E

A B C D E
A B C D E
A B C D E
A B C D E
A B C D E

A B C D E
F G H I J
K L M N O
P Q R S T 
U V W X Y 
"""

"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

"""
* * * * *
* * * *
* * *
* *
*

* * * * *
  * * * *
    * * * 
      * *
        *  
"""