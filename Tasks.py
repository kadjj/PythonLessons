# 1) Write a program that will convert the sequence of numbers entered by the user into text, e.g .:

if __name__ == "__main__":
    numbers = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    user_input = input("Choose a number: \n")
    output_str = " "
    for elem in user_input:
        output_str += numbers[int(elem)] + " " #output_str = output_str + numbers[int(elem)]
    print(output_str)

#2) Create a function that takes a list of integers and returns what the smallest number is in.

def get_min_index(lst):
    min_value = lst[0]
    min_index = 0

    for idx, value in enumerate(lst):
        if value < min_value:
            min_value = value
            min_index = idx

    return min_index, min_value
"""
small=0
for i in rage(len(list))
    if i - 0:
        small < list[i]
    if small < list[i]:
      small = small
    else:
        small + list[i]
"""


if __name__ == "__main__":
    int_list = [343, 53, 43, 2, 566, 90, 64]
    idx, value = get_min_index(int_list)
    print(f"The smallest value in the list is: {value}, it is in position: {idx}")

#3)Create a function that checks that the number given in the argument is prime.
# The function should take a numeric value and return a logical value of True / False.

from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(f"11: {is_prime(11)}")
    print(f"12: {is_prime(12)}")

#4)Create a function that checks if the string given as an argument is a palindrome
# (ie reading backwards and forwards is exactly the same, eg "kayak", "madam").
def is_palindrom(napis):
    napis = napis.lower()
    return napis == napis[::-1]


if __name__ == "__main__":
    print(is_palindrom("Madam"))
    print(is_palindrom("kayak"))
    print(is_palindrom("Ala has a cat"))

#5) Create a function that will calculate the number of upper and lower case letters in a string.
def count_upper_lower_case(sentence):
    no_upper_case, no_lower_case = 0, 0

    for char in sentence:
        if char.islower():
            no_lower_case += 1
        elif char.isupper():
            no_upper_case += 1

    return no_upper_case, no_lower_case


if __name__ == "__main__":
    napis = "The quick Brown Fox"
    upper, lower = count_upper_lower_case(napis)
    print(f"Number of uppercase letters: {upper}, number of lowercase letters: {lower}")

#6)Write a function that takes two strings and checks to see if they are anagrams of each other.

def are_anagrams(napis1, napis2): # you can also use, for example, Counter
    napis1 = sorted(napis1.lower().replace(" ", ""))
    napis2 = sorted(napis2.lower().replace(" ", ""))
    return napis1 == napis2


if __name__ == "__main__":
    print(are_anagrams("Tom Marvolo Riddle", "I am Lord Voldemort"))
    print(are_anagrams("Ala has a cat", "Cat has Ala"))

