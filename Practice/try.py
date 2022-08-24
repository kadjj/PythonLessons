
"""
leap_year
    Write a program that asks the user to enter the year
     and then checks if the year is a leap year.

     A year is leap when it divides by 400 or when it divides
     by 4, but is not divisible by 100.


year = int(input("Name a year: "))
if year % 4== 0:
    print("Year " + str(year) + " is a leap year")
else:
    print("Year " + str(year) + " is not a leap year")
"""
"""
max_min_list
    Write a program that displays
     the smallest and largest item in a list, and will reverse it.

list1 = [8, 9, 10, 5, 4, 12]
list1.reverse()
print(max(list1), min(list1), list1)
"""

"""
Notebook
    Create a Notebook class that will contain the fields: manufacturer, net price and RAM memory.
     Add methods to calculate the gross price (+ 23% VAT) and increase the amount of RAM.
     
     
     
"""
"""
Set_defference    
    Ask the user for items to be added into two lists.
     To do this, the user first adds to the first list until he enters a zero.
     Then it adds to the second list until it types zero again.
     Create sets out of these two lists.
     Your task is to display the sorted symmetric difference of the sets created from these two lists.



"""
"""
    Write a program that asks the user for a natural number (N) and prints all numbers from 1 to N squared (for loop).
"""
"""list comprehension
"""
old_list = [1, 2, 3, 4, 5, 6, 7]
new_list = [x ** 2 for x in old_list if not x % 2] # if not x%2 is same as if x%2==0
print(new_list)


numbers = { 0 : "zero",
        1 : "one",
         2 : "two"
}
number = input("Say a number: ")
answer = " "
for i in number:
    answer += numbers[int(i)] + " "
print(answer)