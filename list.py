"""
List is a collection of items in Python.
List is a mutable sequence of items.
List is a ordered sequence of items.
# """
# myList = [12,"Royal",12.5,True,2+5j]

# print(myList)
# print(type(myList))

# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[3])
# print(myList[4])
# # print(myList[5])

# print(len(myList))
# # print(max(myList))

# print(myList[-1])
# print(myList[1:3])
# print(myList[::-1])

# myList = [12,34,56,78,90,2,43,64,7,8,1,6,9,90]

# print("Length of the List:",len(myList))

# print("Max Value in the List:",max(myList))
# print("Min Value in the List:",min(myList))
# print("Sum of the List:",sum(myList))   # sum of all the elements in the list
# print("Sort of the List:",sorted(myList))
# print("Reverse of the List:",myList[::-1])
# print("Sort of the List:",sorted(myList,reverse=True))

# list1 = ["apple","banana","cherry","Apple","Mango"," "]
"""
Ascii 

A - 65 
B - 66....

a - 97
b - 98....

(_)space - 32
# """
# print("List1:",list1)
# print("List1 Length:",len(list1))
# print("List1 Max:",max(list1))
# print("List1 Min:",min(list1))
# # print("List1 Sum:",sum(list1))
# print("List1 Sort:",sorted(list1))
# print("List1 Reverse:",list1[::-1])
# print("List1 Sort:",sorted(list1,reverse=True))

l = [2,3,56,43,4,5,6,7,8,9,10,13,56]

print(l.append(12))
print("List after append:",l)

l1 = l.copy()
print("List1 after copy:",l1)

l2 = l
print("List2 after copy:",l2)

print(id(l))
print(id(l1))
print(id(l2))

print(l is l1)              
print(l is l2)

l1.clear()
print("List1 after clear:",l1)

del l1
# print("List1 after del:",l1)

print(l.count(56))

l.extend(l2)
print("List after extend:",l)

l.insert(5,12)
print("List after insert:",l)

print(l.index(56))

print(l.pop(5))
print("List after pop:",l)

l.remove(56)
print("List after remove:",l)

# l.remove(56,12)
# print("List after remove:",l)

l.reverse()
print("List after reverse:",l)

l.sort()
print("List after sort:",l)

l.sort(reverse=True)
print("List after sort:",l)

"""
Task:
    1. add 5 numbers into the list and print the list
    2. add 10 numbers into the list, reverse that list, store the list into another list and print the list
    3. add 10 numbers into the list, sort that list and print the list
    4. Create a list of numbers and sort it in descending order.
    5. add 10 numbers into the list, print the maximum and minimum number from the list
    6. add 10 numbers into the list, print the average of the list
    7. add 10 numbers into the list, print the sum of the list
    8. scan 5 numbers from the user and store it into the list, check if both the lists are same or not
    9. Create a list of numbers and sort it in ascending order.
    10. Wap to find no. of month from the given no. of days
    11. wap to scan seconds and print hour, minute and remaining seconds
    12. wap to swap 3 numbers that is scanned by the user (a->b, b->c, c->a)
    13. wap to check whether the number is odd or even
    14. wap to find out the maximum, minimum, average of the numbers that is scanned by the user
    15. wap to make any user inputted string in uppercase or lowercase
    16. wap to print the sum of user entered numbers (scan by the user)
    17. Write a program to find the number of vowels, consonents and white space characters in a given string.
        Example:
            input string: Python Programming
            output:
                vowels: 4
                white spaces: 1
                consonents: 13
"""

input_string = input("Enter the string: ")
print("String:",input_string)

input_string = input_string.lower()
vowels = input_string.count("a") + input_string.count("e") + input_string.count("i") + input_string.count("o") + input_string.count("u")

white_spaces = input_string.count(" ")

consonents = len(input_string) - vowels - white_spaces

print(f"Vowels: {vowels},White Spaces: {white_spaces},Consonents: {consonents}")
print("Vowels:",vowels,"White Spaces:",white_spaces,"Consonents:",consonents)