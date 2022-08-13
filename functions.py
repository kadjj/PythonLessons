"""
A function is a block of code/sentenses that runs only when it is called
- can have parameters, i.e. it can accept input
- it can return a result

def <<function_name>>(): # a function without parameters and does not return a value/result
    sentences
def <<function_name>>(): # a function without parameters and returns a value/result
    sentences
"""

def print_name():
    name = input("Your name: ")
    print(f"What a nice name {name}!!")

#call a function by its name
print_name()

def return_name():
    name = input("Your name: ")
    return name
fname = return_name()
print(f"Your have a lovely name {fname} ")
"""
ARGUMENTS and information passed into a function
def <<function_name>>(<<argument>>, ....., <<argument>>):
    sentences
    return <<data>>
"""

def my_name(name, age):
    print(f"Your have a lovely name {name} for your {age} ")
my_name("Kadipadi", 20)
my_name(30, "Kats")
my_name(age=10, name="Kata")    #named arguments


#calling your function
# func_name(<<name_param>> = value)

def area_of_square(length):
    return length ** 2

def area_of_rectangle(len, breath):
    return len * breath
def get_shape(len, breadth):
    if len == breadth:
        area = area_of_square(length=len)
        print(f"Shape is a square with area {area}")
    else:
        print(f"Shape is a rectangle with area {area_of_rectangle(len, breadth)}")
get_shape(len=10, breadth=8)
get_shape(10, 10)
"""
you can have default values for your functions, such that, if no arguments is passed, 
the default value is used"""

def isogram(word)
    l = [x for x in word.lower()]
    if len(set(l)) :