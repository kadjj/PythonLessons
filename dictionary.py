"""
key: value pair
it is ordered
it is changeable
keys do not allow duplicate
<<dictionary_name>> = {
<<key>>: <<value>>,
<<key>>: <<value>>
}
they are the foundation of many other collections

"""

std = {
    'name' : 'Kadi',
    'age' : 28,
    'occupation' : 'Data Specialist'
}

"""
Access items in a dict:
- using keys as index, returns error if key doesn't exist
- use get method, returns non, if key doesn't exist
<<dict_name>>.get(<<get_to_get>>)
"""
print(std["age"])
print(std.get("age"))

"""get all keys
- keys method returns a list of all the keys in a dict
<<<dict>>>.keys()
"""
print(std.keys())
print()

"""add items to a dict:
-use key_value pair
    <<dict>>[ <<new_key>>] = <<value>>
- update()
    <<dict>>.update({
        <<key>>: <<value>>,
        <<key>>: <<value>>
    })
"""
#if key exists already, it replaces the value, if it doesn't exist, it adds a new key
std['is student'] = 'No'
std['name'] = 'Kadi Jõesaar'

"""remove items in a dict:
 - pop: generates errot if key doesnt exist
 <<dict>>.pop(<<key>>)
 - popitem(): removes the last item that you added in the dictionary
 - clear(): empties your dictionary
 """

std.pop("occupation")
print(std)

"""
Loop though a dict:
-values() : returns the values in the dict

"""
for item in std: #returns the key or use <dict<.keys()
    print(item)
    print(item, std[item])

for val in std.values(): #returns dict values
    print(val)

for key, val in std.items(): #returns dict values and key
    print(f"{key}: {val}")

"""dictionary comprehension"""
print({k : v for k,v in std.items()})
print({k : str(v).upper() for k,v in std.items()}) #str makes the age a string

""" nested dictionary
<<dict>> = {
<<key>> :  {
        <<key>>:<<value>>
        ...
        <<key>>:<<value>>
    },
<<key>> :  {
        <<key>>:<<value>>
        ...
        <<key>>:<<value>>
    }
...
}
"""

students = {
"Kadi" :  {
        "is student" : "True",
        "age" : 20
    },
"Thomas" :  {
        "is student" : "False",
        "ages" : 30,
        "hair": "brown"
    }
}
print(students.keys())

"""
     Write a program that takes a number N from the user, then creates a dictionary of keys 1 through N with values that are the squares of the keys.
"""
N = int(input("Give a number: "))
dictionary = {}

for i in range(1, N + 1):
    dictionary[i] = i**2
for key, value in dictionary.items():
    print(f"the square of {key} is {value}")
