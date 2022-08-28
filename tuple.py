"""
Tuples
-------
    - It is one of the collection of python.
    - It is a sequence type.
    - It is ordered.
    - it iss immutable.
    - Allow Multiple data types
    - Allow duplicates values
"""

# myTup = (12,"Royal",25.52,2+5j)

# print("Type of variable muTup is: ",type(myTup))
# print(myTup)

# for i in myTup:
#     print(type(i))
#     print(i)

# print(myTup[0])
# print(myTup[-1])

# t = (1,2,3,5,9,8,10,56,78,74,68,80)

# print("Length of the tuple is:",len(t))
# print(max(t))
# print(min(t))
# print(sum(t))
# print(sorted(t))
# print(sorted(t,reverse=True))


# # t[0] = 100

# t2 = (15,)

# print("Type of variable t2 is: ",type(t2))

# t3 = "Hey","Hello","World"

# print("Type of variable t3 is: ",type(t3))

# t4 = 85,98,26,78

# print("Type of variable t4 is:",type(t4))

# print(t4)

# t5 = ()

# print("Type of variable t5 is:",type(t5))
# print(t5)

# t6 = tuple()

# print("Type of variable t6 is:",type(t6))

# print(t6)


# t = (1,2,3,5,9,8,10,56,78,74,68,80)

# print(t.count(78))

# print(t.index(78))

# l = []

# n = int(input("Enter number of elements: "))

# for i in range(n):
#     l.append(int(input("Enter element: ")))

# t = tuple(l)

# print(sum(t))

"""
Unpacking of tuple
"""

# t = "apple","banana","cherry","mango"

# red,green,yellow = t

# print(red)
# print(green)
# print(yellow)

t1 = (1,2,3,4,5,6,7,8,9,10)

num1 , num2 , *num3 = t1
print(num1)      # 1
print(num2)      # 2
print(num3)      # [3,4,5,6,7,8,9,10]


num1 , *num2 , num3 = t1
print(num1)      # 1
print(num2)      # [2,3,4,5,6,7,8,9]
print(num3)      # 10



*num1 , num2 , num3 = t1
print(num1)      # [1,2,3,4,5,6,7,8]
print(num2)      # 9
print(num3)      # 10


a ,b, c, *d, e = t1

print(a)
print(b)
print(c)
print(d)
print(e)

l = [(1,2,3),(2,3),[12,13]]

print(l)

print(l[2][1])
