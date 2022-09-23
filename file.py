"""
File Handling / Management

--> txt, csv(comma separated values), json ....

1) Create file 
2) Read 
3) Delete
4) Update

modes
-------

r --> read
x --> new file create and it will generate error for existing files
w --> create new file and overwrite existing file
a --> append 
"""

"""
Syntax:
------------

var_name = open("file path",mode)

"""

# f = open("sample.txt","r")

# print(f.read())          # it reads whole file

# f.close()

# f = open("sample.txt","r")

# print(f.read(10))          # it reads first 10 characters of the file

# f.close()

# f = open("sample.txt","r")

# print(f.readline())          # it reads one line from the  file
# print(f.readline())

# f.close()

# f = open("sample.txt","r")

# print(f.readlines())         

# f.close()

# f = open("sample.txt","a")

# f.write("\nHi!! i am additional DATA")

# f.close()

# f = open("data.txt","x")              # it creates new file and if file already exists then it gives error

# f.write("New file created")

# f.close()

# f = open("file1.txt","w")         # it creates new file but if file exists then it overwrite whole content

# # f.write("New file is Created by w mode")
# f.write("Oops!! Data is deleted")
# f.close()


"""
Make a file with 5 statements given by user
"""
"""
Make a file named Number.txt and store 10 numbers into them. And print odd numbers and find sum of the even numbers from them.
"""

# f = open("Number.txt","w")

# for i in range(10):
#     f.write(input("Enter number: "))

# f.close()

# f = open("Number.txt","r")
# sum = 0
# m = f.read()
# print(m)
# for i in m:
#     if int(i) % 2 == 1:
#         print("Odd number is: ",i)
#     else:
#         sum += int(i)
    # print(i) 

# print("Addition of even numbers are: ",sum)


# f = open("Number.txt","w")
# o = open("odd.txt","w")
# e = open("even.txt","w")
# for i in range(10):
#     f.write(input("Enter number: "))

# f.close()

# f = open("Number.txt","r")

# m = f.read()
# # print(m)
# for i in m:
#     if int(i) % 2 == 1:
#         o.write(i)
#     else:
#         e.write(i)

"""
Error Handling
-------------------

1. try ---> it will execute code
2. except ---> it will execute when error occurs in try block
3. else  ---> it will execute when no error occurs in try block 
4. finally ---> it will execute if error occurs or not.
"""

# print(x)


# try:
#     print(x)
# except:
#     print("Exception Occured")

# try:
#     print(x)
# except NameError:
#     print("NameError Occured")
# except:
#     print("Another error occured")

# x = "Hello"

# try:
#     print(x)
# except:
#     print("Exception Occured")
# else:
#     print("No Error Generated")
# finally:
#     print("Finally Block Executed")

# try:
#     f = open("Number.txt","x")
# except:
#     f = open("Number.txt","w")
#     f.write("Hello")
# else:
#     f.write("Hye")
# finally:
#     f.close()

# x = -1

# if x < 0:
#     raise Exception("No Number below zero")

# x = "Hello"

# if type(x) is not int:
#     raise TypeError("Only Integers allowed")