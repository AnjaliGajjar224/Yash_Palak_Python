"""
Bitwise Operators

1) & - Bitwise AND
2) | - Bitwise OR
3) ^ - Bitwise XOR
4) << - Left Shift
5) >> - Right Shift
"""

# print(45>>2)
# print(35>>2)
# print(56>>5)
# print(62>>3)

# print(45<<2)
# print(53<<3)
# print(74<<2)
# print(12<<6)

"""
Logical Operators

1) and - Logical AND(&&)
2) or - Logical OR(||)
3) not - Logical NOT(!)
"""

# a = 15
# b = 10
# c = 5

# print(a>b and b<c)       # True and False = False
# print(a>b or b<c)        # True or False = True
# print(not(a>b and b<c))  # not (True and False) = True

"""
Membership Operators
1) in 2) not in
"""

# print('ban' in 'banana')
# print('k' in 'banana')

# print('b' not in 'banana')
# print('k' not in 'banana')

"""
Take a string from the user and take a another string or character from the user and find out that character is in the string or not
"""


"""
Identity Operators
1) is 2) is not
"""

# a = 15
# b = 15
# c = 10

# print(id(a))
# print(id(b))
# print(id(c))

# print(a is b)
# print(a is c)

# print(a is not b)
# print(a is not c)

"""
Sequence Data Types

1) String
2) List
3) Tuple

String is immutable & ordered.
"""
# ch = 'Apple'
# print(type(ch))
# print(ch)

"""
     Positive Indexing
A  ---> 0
p  ---> 1
p  ---> 2
l  ---> 3
e  ---> 4
"""
# print(ch[0])
# print(ch[1])
# print(ch[2])
# print(ch[3])
# print(ch[4])

# print(len(ch))

"""
    Negative Indexing
A   -5
p   -4
p   -3
l   -2
e   -1

"""

# print(ch[-1])
# print(ch[-2])
# print(ch[-3])
# print(ch[-4])
# print(ch[-5])

"""
Slicing - Extracting a Substring

    1) [start:stop:step]
    2) [start:stop]
    3) [start:]
    4) [:stop]
    5) [:]
"""
# myStr = "Python is a Programming Language"

# print(len(myStr))
# print(myStr)
# print(myStr[15])
# print(myStr[0:15])
# print(myStr[10:29])
# print(myStr[:])
# print(myStr[10:])
# print(myStr[:10])
# print(myStr[-19:-1])
# print(myStr[-19:])
# print(myStr[:-16])
# print(myStr[2:30])
# print(myStr[2:30:2])
# print(myStr[2:30:3])
# print(myStr[::5])
# print(myStr[-1:-25])
# print(myStr[19:2])

# print(myStr[::-1])
# print(myStr[::-2])
# print(myStr[19:0:-1])
# print(myStr[-1:-25:-1])

myStr = "royal_Technosoft_Pvt_Ltd."

print(len(myStr))
print(myStr.center(48))   # 48 - length of the string = 48 - 24 = 24/2 = 12
print(myStr.center(48, '*'))
print(myStr.center(47, '-'))

print(myStr.capitalize())
print(myStr.casefold())
print(myStr.count('o'))
print(myStr.count('o', 0, 10))
print(myStr.count('o', 0, 15))

print(myStr.count('_'))

print(myStr.encode())         # Encodes the string into bytes UTF - 8
print(myStr.encode('ascii'))   # Encodes the string into bytes ASCII
print(myStr.encode('utf-8'))   # Encodes the string into bytes UTF - 8

# from encodings.aliases import aliases

# print(aliases)

print(myStr.endswith('Pvt_Ltd.'))

print(myStr.endswith('d'))


text = "Python\tis\ta\tProgramming\tLanguage"

print(text)
print(text.expandtabs(20))
