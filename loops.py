"""For and While Loops

While loop: executes a set of sentence until the condition is no longer valid
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

"""For loop in a string - iterates over a string (sequence) by characters (letters)"""
"""
string = "Pyhton"
for chr in string:
    if chr == "t":
       break

    print(chr)

list = ["English", "Germain", "French", "Spanish"]
for language in list:
    print(language)

for count in range(1,8,2):
    print(count)

count = 1
while count <= 5:
    print(count)
    count += 1
"""

"""number = int(input("Enter an integer: "))
for count in range(1,11,2):
    answer = number * count
    print(number, "x", count, "=", answer)



answer = 0
for x in range(1,101):
    answer = answer + x
print(answer)
"""

N = int(input())
sum = 0
for i in range(0,N):
    sum = sum +i
    i+=1
print(sum)




