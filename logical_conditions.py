"""
Logical conditions evaluates to boolean (True, False)
a == b
a!= b
a < b
a > b

"""
if 10 < 5:
    print("10 is less than five")
else:
    print("10 is not less than 5")

marks = [90, 75, 80, 60, 72]
grade = []

for mark in marks:
    if mark >= 90:
        grade.append("A")
    elif mark >= 80 and mark < 90:
        grade.append("B")
    elif mark >= 70 and mark < 80: #70>= mark < 80
        grade.append("C")
    else:
        grade.append("Repeat")
70>= mark < 80
print(grade)

""""
Tenary Operations / Conditional expressions
<<value_if_true>> if <<condition>> else <<value_if_false>>
"""
print("not equal") if 10 != 5 else print("equals")

weight = int(input("Weight: "))
height = float(input("Height: "))
if (weight / height ** 2) < 18.5:
    print("Under")
elif (weight / height ** 2) >= 25:
    print("over")
else:
    print("normal")

weight = float(input("Weight: "))
height = float(input("Height: "))
BMI = weight / height ** 2
if BMI < 18.5:
    print("Under")
elif BMI >= 18.5 and BMI <25:
    print("normal")
else:
    print("over")


number = int(input("Pic a number: "))
if number %2 == 0 and number > 0:
    print("Your number is even number")
elif number == 0:
    print("Your number is zero")
elif number %2 != 0 and number > 0:
    print("your number is odd")
else:
    print("your number is negative")


year = int(input("Name a year: "))
if year % 4== 0:
    print("Year " + str(year) + " is a leap year")
else:
    print("Year " + str(year) + " is not a leap year")