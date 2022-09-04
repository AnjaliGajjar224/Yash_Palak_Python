"""
Dictionary is also one of the collection of Python.
Dictionary is unordered.
Dictionary is immutable.
It contains Key - value pairs.
"""

# myDict = {
#     'a': 'apple',
#     'b': 'banana',
#     'c': 'cat'
# }

# """
# a , b, c --> Keys
# apple, banana, cat ---> Values
# """

# print(myDict)

# print(myDict['a'])
# print(myDict['b'])
# print(myDict['c'] )

# Dict1 = myDict.copy()

# print(Dict1)

# Dict1.clear()
# print(Dict1)

# Dict2 = {}

# x = "key1","key2","key3"
# y = 0 ,1 , 2

# print(Dict2.fromkeys(x,y))

# print(myDict.get('a'))
# print(myDict.get('b'))
# print(myDict.get('c'))

# print(myDict.items())

# print(myDict.keys())

# for i in myDict.items():
#     print(i)

# print(myDict.pop('a'))
# print(myDict)

# print(myDict.popitem())
# print(myDict)

# myDict.setdefault('m','mango')

# print(myDict)


# myDict.setdefault('b','cherry')
# print(myDict)


# myDict.update({'b':'cherry'})
# print(myDict)

# print(myDict.values())

c1 = {
    1 : 'apple',
    2: 'orange',
}

c2 = {
    '&': 123,
    '#': 456
}

c3 = {
    'a': 125.56,
    'b': 'cherry'
}

d = {
    'aa' : c1,
    'bb' : c2,
    'cc' : c3,
    'dd' : {
        1 : 12345,
        2 : 45678
    }
}

print(d)

print(d.get('aa'))

print(d['aa'][2])
print(d['cc']['b'])
"""
1. SignUp
2. Login
3. Exit

---> 1 

Username , password ---> data will stored in dictionary

---> 2

username , password

if username exist:
    check password
          ---> Successfully login
    wrong password
        ---> Forgot Password?
else:
    User not found
    You have to SignUp first.
"""