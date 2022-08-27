"""
errors terminates the python code been executed
- syntax error/parser error
        - shows the error with ^
        - most IDE (integrated development environment) catches this error
- exceptions: errors that occur during execution
    - code is syntactically correct
    - but error occurs whey you try to execute your code
Exception handling:
try: block of code that might generate error / run this code
except: handle the exception
else: execute code when there is no error
finally: executes whether an error occurs or no

"""
try:
    print(10/2)
except:
    print("Do nothing")
else:
    print("no error")
finally:
    print("I occur regardless of an error")

try:
    x= 10
    y= [10, 2, 3, 0, 4, 6]
    z= [x/m for m in y]
except:
    print("error")
finally:
    print("I occur regardless of an error")

"""
Example: database connection
try: make a connection
except: error
finally: close the connection

read and write to a file
try: read the file
except: error that occurs during reading of the file
else/finally: close the file
"""
"""
Types of Exceptions:
- TypeError – operation/function performed with wrong type of object (e.g. '2' + 2)
- KeyError – the key (eg in a dictionary) could not be found
- IndexError – an attempt to get to a non-existent element (e.g. in a list)
- ModuleNotFoundError –imported (entire) module could not be found
- AssertionError – the assertion (used e.g. in tests) fails
- NameError – object cannot be found (e.g. variable before declaration)
- SyntaxError – invalid syntax (e.g. expression: a (=): 1 + 2))
- ZeroDivisionError – division by zero
Warnings are not exceptions.       
"""
"""Multiple exceptions"""

try:
    print(name)
except NameError as err: #named exceptions
    msg = err
    print(f"a new message: {err}")
except:
    print("other errors")

"""Creating customized Exceptions"""
class NoNegativeInList(Exception):
    pass


"""raise exceptions - when you need to create an exception"""
list1 = [10, 4, 5, -1, 7, 7]
for x in list1:
    if x <0:
       # raise Exception("Negative values not allowed")
        # raise IndexError("Index Error: Negative values not allowed")
        raise NoNegativeInList("Negative values not allowed")

