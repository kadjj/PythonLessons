

"""Write a program that takes a number N from the user, then
    creates a dictionary of keys 1 through N with values that are the squares of the keys."""
"""


    Write a program that reads a text file and then prints it with numbered lines.
"""

f = open("test.txt")
i = 0
while i < 10:
    i = i + 1
    print(str(i) + ") " + str(f.readline()))

"""Q1 given 2 strings, ca you make first string from the second by deleting some caracters s1="Hello" s2="dkbakdalskf"
- join strings
"""
s1 = "Hello"
s2 = "lksHhflekslgkojk"
count = 0
for ch in s1.lower():
    if ch in s2.lower():
        count += 1
    print(count)
    if count == len(s1):
        print("Possible")
    else:
        print("Impossible")

"""Q2 sum numbers until flag -9999 is seen
methods: you can save the numbers in a list and compute, you can use while loop
"""

"""list = [10, 23.4, 67, -9999, 7, 8, 100]
i = 0
while i < len(list):
    element = list[i]
    print(len(element))
    i += 1"""

"""find the max and min of set of numbers"""
set = {10, 2, 15, 19, 20, 4, 7}
print("Max value of the set is: ", max(set))
print("Min value of the set is: ", min(set))

"""count the number of odd and even elements in a list"""
list = [10, 11, 12, 13, 17, 18, 10]
"""
def counter_using_loop(nums:List) ->tuple

i = 0
while i < len(list):
    if i %2==0:
        print(count())
    else:
       print(count())
    i += 1
"""
