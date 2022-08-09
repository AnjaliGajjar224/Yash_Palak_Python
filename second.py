"""
Input from the user:
# """
# print("Enter Number 1:")

# num1 = int(input())
# print(type(num1))
# num2 = int(input("Enter Number 2:"))

# add = num1 + num2

# print("Addition of",num1,"and",num2,"is",add)

"""
Syntax:
------------
1) if condition:
    code

2) if condition:
        code
    else:
        code

3) if condition:
        code
    elif condition:
        code
    else:
        code
"""

from cgi import print_arguments


num1 = int(input("Enter Number 1:"))
num2 = int(input("Enter Number 2:"))

if num1 > num2:
    print("Number 1 is greater than Number 2")
else:
    print("Number 1 is less than Number 2")

"""
Task:
----------
1) Wap to find odd/even
2) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    # Ask user for quantity
    # Assume each unit's cost is 100.
    # Judge and print total cost for user. 

3) A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

4) A student will not be allowed to sit in exam if his/her attendance is less than 75%.
    # Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print:
    # percentage of class attended
    # Is student is allowed to sit in exam or not.

5) Take 3 numbers from the user and find maximum

6) A school has following rules for grading system:
    # a. Below 25 - F
    # b. 25 to 45 - E
    # c. 45 to 50 - D
    # d. 50 to 60 - C
    # e. 60 to 80 - B
    # f. Above 80 - A
    # Ask user to enter marks and print the corresponding grade.
 
"""