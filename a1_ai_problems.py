# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

# 1. Sum of Two Numbers
# Write a function `sum_two_numbers` that takes two numbers as arguments and returns their sum.
def sum_two_numbers(n1, n2):
    return n1+ n2
# 2. Convert Celsius to Fahrenheit
# Write a function `celsius_to_fahrenheit` that converts a temperature from Celsius to Fahrenheit.
# Use the formula: F = C * 9/5 + 32
def celsius_to_fahrenheit(temp):
    return temp * 9/5 + 32
# 3. Check Even or Odd
# Write a function `is_even` that returns `True` if a given number is even, and `False` otherwise.

# 4. List Length
# Write a function `list_length` that returns the length of a given list.

# 5. Find Minimum in List
# Write a function `find_minimum` that finds and returns the smallest number in a list of numbers.

# 6. Repeat a String
# Write a function `repeat_string` that takes a string and a number as arguments and returns the string repeated that many times.

# 7. Count Words in String
# Write a function `count_words` that counts the number of words in a given string.
# Assume words are separated by spaces.

# 8. Square a Number
# Write a function `square_number` that takes a number as an argument and returns its square.

# 9. List Contains Number
# Write a function `contains_number` that takes a list and a number as arguments and returns `True` if the number is in the list, and `False` otherwise.

# 10. Find the First Element
# Write a function `first_element` that returns the first element of a list. If the list is empty, return `None`.

