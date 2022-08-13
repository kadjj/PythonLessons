"""
ZIP:
easily combine 2 lists

in order to see content if a zio, it must be casted to a list
if different lenghts, the result will be the shortest list
"""

name = ["Kadi", "Margus", "Rosalii", "Ines" ]
surname = ["Joesaar", "Kodu", "Koduu", "Kodu"]
age = [25, 40, 3, 5]

print(list(zip(name, surname, age)))