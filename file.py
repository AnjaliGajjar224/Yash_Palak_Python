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
# Reading File

# f = open("file1.txt","r")

# print(f.read())      # Read whole file

# f.close()       # Used to close file


# f = open("file1.txt","r")

# print(f.read(20))          # It only reads first 10 characters of file

# f.close()       # Used to close file


# f = open("file1.txt","r")

# print(f.readline())            # it reads one line at a time
# print(f.readline())

# f.close()       # Used to close file


# f = open("file1.txt","r")

# print(f.readlines())

# f.close()       # Used to close file



# Append File


# f = open("file1.txt","a")


# f.write("\nI am an Additional DATA")
# f.write("\n")
# f.close()

# f = open("file1.txt","r")
# print(f.read())
# f.close()


# CREATE FILE

# f = open("sample.txt","x")

# f.write("I am aNEW FILE!!")

# f.close()

# f = open("sample.txt","w")

# f.write("Oops!! This is New DATA")

# f.close()


# f = open("sample.txt","w")

# f.write("Oops!! Your PAST DATA IS DELETED")

# f.close()

"""
Make a file named sample.txt and write 5 statements into file given by user.
"""