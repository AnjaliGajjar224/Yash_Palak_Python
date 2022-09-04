"""
Set is one of the Collection of Python.
Set is mutable.
Set is unordered.
Set doesn't allows duplicates values.
"""

# mySet = {1,2,3,4,5,1,2,3}

# print(mySet)
# print("Type: ",type(mySet))
# print("Length: ",len(mySet))

# mySet = {12,13,21,54,7,89,90,1,0}

# print(mySet)

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}

# set1.add(9)                 # add element into set

# print(set1)

# # s = set()

# # print("Type: ",type(s))

# print(set1.difference(set2))               # set1 - set2 = {1,2,3}

# # set1.difference_update(set2)
# print(set1)


# print(set1.symmetric_difference(set2))        
# # print(set1)

# # set1.symmetric_difference_update(set2)
# print(set1)

# set1.discard(9)
# print(set1)

# print(set1.intersection(set2))

# # set1.intersection_update(set2)
# print(set1)

set3 = {1,2,3}
set4 = {4,5,6}
set5 = {1,2,3,4,5,6}

print(set3.isdisjoint(set4))              # if intersection is null, then returns True

print(set3.isdisjoint(set5))

print(set3.issubset(set5))               
print(set4.issubset(set3))

print(set5.issuperset(set4))

print(set3.pop())
print(set3)

print(set3.remove(2))
print(set3)


set3.discard(5)
print(set3)

# set3.remove(5)
print(set3)

print(set3.union(set4))

set3.update(set4)
print(set3)
