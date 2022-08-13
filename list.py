"""
lists are used to stor multiple values in a variable
list are denoted/created using [ ]
list are ordered collection of items
allow duplicates
changeable - add, remove, replace
"""

mylist = ['apples', 'mangoes', 2, 7.5, 'red']
print(type(mylist))
print(mylist[0])
print(mylist[-1])
print(mylist[2:4])
# use in to check if a value exists in a list
print('guava' in mylist)

"""
add items to a list
- append: adds to the end of a list
- insert: adds at a specific index
<<list>>.insert(<<position>>, value)
- extend: appends elements from a list to another list, appends at the end
<<current_list>>.extend(<<new list>>)
"""

mylist.append('guavas')
mylist.append('grapes')
mylist.insert(2, 'blueberries')
mylist.insert(0, 'mangoes')
print(mylist)

exotic_fruits = ['cashew', 'wild blueberries', 'passion fruit']
mylist.extend(exotic_fruits)

mylist[4] = "corn"
print(mylist)

"""
remove items in a list:
 - remove: <<list>>.remove(<<item>>) 
        - with duplicate instances, the first is removed
 - pop: removes the last item
 <<list>>.pop(<<index>>): removes item at the last position
  - clear: removes all items in a list (content of the list)
 
"""
mylist.remove(7.5)

mylist.pop()
print(mylist)
mylist.pop(1)
print(mylist)
exotic_fruits.clear()
print(exotic_fruits)

age = [12, 14, 25, 67, 13, 19]
print(min(age))
print(max(age))
print(sum(age))
print(sum(age) / len(age))

mylist.sort()
age.sort()
print(mylist)
print(age)

mylist.reverse()
print(mylist)

"""
looping though a list
- for loop
for <<variables>> in <<list>>:
statement

"""

for var in mylist:
    print(f"I love {var}")    # f string use curly brackets
    # print("I love " + var)
    # print("I love {}" .format(var))

name = "Kadi"
ages = 10
print("my name is " + name + "I am " + ages + "years old.")
print("my name is {} and I an {} years ols".format(name, ages))

for item in age:
    print(item/2)
range(10) # from 0 to 9
range(5, 10) # from 5 to 9
range(5, 10, -1) #from 9 to 5 with -1 step

"""
range (start, stop, step)
default step is 1

"""

for i in range(len(age)):
    print(f"index {i}: {age[i]}")

"""
    list comprehension
    - short method of creating a list from an existing list
    - filter and perform operations
    
    """
x = [print(f"My age is {x} ") for x in age]
new_age = [x for x in age if x%2 == 0]

upp_list = [var.upper() for var in mylist]
print(upp_list)
