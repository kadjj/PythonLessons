import os
"""File operations:
- creating a file
- reading a file
- updating a file
- deleting

open(<<filename>>, <<mode>>)

Modes:
r = read => default, opens file for reading, error if file does not exist
w = write - open the file for writing (starts in the beginning of the file), creates file if not exists
a = append - open the file for appending (goes to the end of the file), if file not exists, it creates the file
x = create - creates a new file, error if file exists

t = text mode => default
b = binary

"""
#read a file
f = open("test.txt")    #this opens the file
print(f.read())         #this starts reading the file
print(f.readline())     #returns line by line
print(f.readline())

"""f = open("test.txt")
while True:
    print(f.readline())
    if not f.readline():
        break
        """
f.close()

f = open("test.txt", "w")
f.write("\n I should take a walk")
f.close()

f = open("test.txt", "a")
f.write("\n because it's a beautiful day. \n hopefully will stay like it. \n if not, then i will watch tv.")
f.close()

# os.remove("test.txt")