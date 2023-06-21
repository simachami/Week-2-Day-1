# Title: Counting Strings Exercise

# Problem Statement:
# You are given two strings, A and B. Your task is to count how many strings equal to A can be constructed using letters from the string B. Each letter can be used only once and in one string only.

# Example:
# Let's take an example to understand the problem better:
# A = "abc"
# B = "abccba"


# Task:
# Your task is to write a Python function that takes in two strings, A and B, and returns the count of strings equal to A that can be constructed using letters from B.
# Input:

# A: A string containing lowercase letters. (3 ≤ A.length ≤ 9)
# B: A string containing lowercase letters. (3 ≤ B.length ≤ 50)
# Output:

# An integer representing the count of strings equal to A that can be constructed using letters from B.


"""
 Look at every letter in string 1, note that letter
 Look at every letter in string 2
 Identify if letter ^ occurs in string 1
 if so: keep a count of said letter
look through counts 
return smallest number
 """

def count_counstructed_strings(string1,string2):
    letter_count = {}
    for letter in string1:
        letter_count[letter] = 0
    for letter in string2:
        if letter in letter_count:
            letter_count[letter] += 1
    return min(letter_count.values())

print(count_counstructed_strings("abc","abccba"))

 

 

    