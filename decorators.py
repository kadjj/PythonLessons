"""
Python
 - create a function inside another function
 - pass a function as an argument to another function

 A decorator is a function that takes another function and extends
 the behaviour of the latter function without explicitly modifying it
"""


def increment_num(num):
    return num + 2


print(increment_num(3))

"""using function as argument"""


def welcome_student(name):
    return f"Welcome {name} from the break"


def did_you_study(name):
    return f"I hope you studies {name}"


def greetings(any_func):
    return any_func("Kadi")


print(greetings(did_you_study))
print(greetings(welcome_student))

"""create a function inside another function - nested function
Inner function are not defined until the parent function is called/executed
Inner function is local to your function, hence they are not available outside the parent"""


def outer_box():  # parent function
    print("This is the parent box")

    def middle_box():  # inner function
        print("This is the middle box")

    def last_box():  # inner function
        print("This is the last box".upper())

    last_box()
    middle_box()


outer_box()

"""function returning another function"""


def greeting(hour):
    def morning(name):
        return f"Good morning {name}"

    def afternoon(name):
        return f"Good afternoon {name}"

    def evening(name):
        return f"Good evening {name}"

    def night(name):
        return f"Good night {name}"

    if hour < 12:
        return morning
    elif hour >= 12 and hour < 17:
        return afternoon
    elif hour >= 17 and hour < 20:
        return evening
    else:
        return night


greet = greeting(22)
print(greet("Kadi"))

"""decorator
- takes a function as an argument
- defines an inner function
- returns the function as the result of its operation
"""


def my_decorator(func):
    def wrapper():
        print(f"this is my wrapper")
        func()

    return wrapper


def say_cheese():
    print("Python is fun")


# say_cheese()
my_decorator(say_cheese)()


@my_decorator
def say_something():
    print("saying something")


say_something()

def increment(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
@increment
def just_a_num(num):
    return num + 3
@increment
def two_nums(num1, num2):
    return num1+3, num2+3

print(just_a_num(5))
print(two_nums(10,8))

"""
a, b, c = (10, 3, 6) : *args == positional arguments

** kwargs == named arguments:
num1 = 3, num2 = 10, num3 = 6

in Python, positional comes before named arguments
"""
def some_example(val1, val2, val3):
    print(val1)
    print(val2)
    print(val3)
    print("Doing smth")
some_example(10, 3, 7)   #positional
some_example(val1 = 10, val2= 6, val3 = 8)   #named arguments
some_example(1, 2, val3 = 3)


def some_example(*args):
    for x in args:
        print(x)
    print("Doing smth")
some_example(10, 3, 7, 8, 5)   #positional


def some_example(**kwargs): #dictionary key value
    for x in kwargs: #just kwargs prints out the keys, kwargs.values() print out the values
        print(x)
some_example(val1 = 10, val2= 6, val3 = 8)   #named arguments
