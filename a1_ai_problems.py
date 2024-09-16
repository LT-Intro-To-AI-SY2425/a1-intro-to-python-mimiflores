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

# Write a function that generates the Fibonacci sequence up 
# to a certain number n. The Fibonacci sequence is a series
#  where the next number is found by adding up the two numbers
#   before it. For example, 0, 1, 1, 2, 3, 5, 8, ...

def fibonacci(n):
    fib_final = []
    a, b = 0, 1
    while a <= n:
        fib_final.append(a)
        a, b = b, a + b
    return fib_final

# Write a function that checks if a given string is a palindrome 
# (a word, phrase, or sequence that reads the same backward as forward).
def isPalindrome(str):
    return s == s[::-1]

# Sure! How about a function that computes the n-th triangular number?
# The n-th triangular number is the sum of the first n natural numbers.

def triangular_number(n):
    # Base case: triangular number of 1 is 1
    if n == 1:
        return 1
    # Recursive case: triangular number of n is n + triangular number of (n - 1)
    else:
        # Complete the recursion here
        pass

# Example usage
print(triangular_number(5))  # Expected output: 15

