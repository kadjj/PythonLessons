"""
- strings in python are arrays
- the first position is 0 for array_like objects
"""
hello = "Welcome to python"

# w = 0, e = 1, l = 2
print(hello[0])
print(hello[4])
print(hello[7])
"""looping though a string
for <<variable_name_for_each_char>> in <<string>>:
statements
"""
for cr in hello:
    print(cr)

"""
lenght in a string: len(<<string>>)
"""
print(len(hello))

"""
check if a character or phrase exist: in
# returns true or false
"""
txt = "it's a beautiful day"
print("beau" in txt)
print("day" not in txt)

""" 
slicing of strings: <<string [<<start_index>>:<<end_index>>]
slice from a position to end: <<string>>[<<start_index>>:]
slice from end to a position: use negative index
"""

print(txt[3:7])
print(txt[7: ])
print(txt[-1]) # returns the last char in array
print(txt[-7:-1])

"""
lower()
upper()
"""
# docs.python.org/3/library/stdtypes.html