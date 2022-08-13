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
""""
print("not equal") if 10 != 5 else print("equals")