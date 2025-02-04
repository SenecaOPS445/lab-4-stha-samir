#!/usr/bin/env python3

# Strings 1
str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(string):
    """Returns a string that contains the first five characters of the argument given."""
    return string[:5]

def last_seven(string):
    """Returns a string that contains the last seven characters of the argument given."""
    return string[-7:]

def middle_number(number):
    """Returns a string containing the second and third characters in the number."""
    return str(number)[1:3]

def first_three_last_three(str_a, str_b):
    """Returns a single string that starts with the first three characters of argument1 and ends with the last three characters of argument2."""
    return str_a[:3] + str_b[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
