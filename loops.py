"""For and While Loops

While loop: excecutes a set of sentence until the condition is no longer valid
"""

i = 10
while i > 3:
    print(i)
    i -= 2      # i = i - 1

"""
break:
stops the loop even if the condition is valid
"""
"""
i = 10
while i > 3:
    print(i)
    if i == 6:
        break
    i -= 2

for x in range (i):
    print(x)
    if x == 6:
        break
"""
"""Continue : stops the current iteration and advances to the next
"""

for x in range (i): #range (start, stop, step)
    if x == 6:
        continue
    print(x)

name = input( "What is your name: ")
print(f"My name is {name}")