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
        result = 0
        for x in range(1, n+1):
            result += x
        return result 

# Implement a function that finds the length of the longest substring without 
# repeating characters in a given string. For example, in the string "abcabcbb",
#  the longest substring without repeating characters is "abc", so the function 
#  should return 3.

def length_of_longest_substring(s: str) -> int:
    start = 0
    max_length = 0
    char_set = set()
    
    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        max_length = max(max_length, end - start + 1)
    
    return max_length

def remove_nth_element(lst: List[int], n: int) -> List[int]:
    """Remove every n-th element from the list until the list is empty.

    Args:
        lst: A list of integers.
        n: The step count for removal (1-based).

    Returns:
        A list of the removed elements in the order they were removed.
    """

    removed_elements = [] 
    index = 0  
    count = 0  

    while lst: 
        count += 1 
        
        if count == n: 
            removed_elements.append(lst.pop(index))  
            count = 0  
        else:
            index += 1
            
        if index >= len(lst):
            index = 0

    return removed_elements