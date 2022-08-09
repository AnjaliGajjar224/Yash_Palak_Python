# # Single line Comments

# """
# Multi
# Line
# Comments
# """

# '''
# Multi
# Line
# Comments
# '''

# # print("Hello World",end="")
# # print('Hey! Good Morning')

# """
# \n - New Line
# \t - Tab
# \b - Backspace
# \r - Carriage Return
# """

# print("Hey! Good\b Morning")

# print("Python is an interpreted language\r1234567")

# """
# Hello\namaste\thank you\bye
# """
# print("Hello\ \bnamaste\ \bthank you\ \bbye")

# print("Hello\\namaste\\thank you\\bye")

# """
# \t is used to represent tab but \\t is used to print \t.
# """
# print("\\t is used to represent tab but \\\\t is used to print \\t.")

# print("\\\\\\\\t")

# """
# Alpha said Beta: "Gamma is teasing Delta, but Gamma said 'I didn't tease Delta, I tease Theta'"
# """

"""
Numeric Data Types
1. Integer
2. Float
3. Complex
"""

a = 100
print(type(a))
print(a)

b = 9898541521231354984213212316545212312312313132131

print(type(b))

c = 2552.5
print(type(c))

d = 152.2598984564531231321352132
print(type(d))
print(d)

e = 1+2j
print(type(e))

f = True
print(type(f))

"""
Arithmetic Operators
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Exponent
7. Floor Division
"""

a = 5
b = 3

print(a,"/",b,"=",a/b)

print(a,"//",b,"=",a//b)      # Floor Division = Integer Division

print(a,"**",b,"=",a**b)      # Exponent 5**3 = 125

print(pow(a,b))

"""
Comparison Operators

1. Equal to   (==)
2. Not Equal to  (!=)
3. Less than    (<)
4. Less than or Equal to    (<=)    
5. Greater than     (>)
6. Greater than or Equal to   (>=)
"""

print(a>b)
print(a!=b)