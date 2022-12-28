"""
LeetCode - 125. Valid Palindrome
25.12.2022
"""

s = "0P"

def isPalindrome(s: str) -> bool:

    formatted_s = []
    for char in list(s):
        if char.isalnum():
            formatted_s.append(char.lower())

    print(formatted_s)

    if formatted_s == formatted_s[::-1]:
        print(f"is a palindrome")
        return True

isPalindrome(s)