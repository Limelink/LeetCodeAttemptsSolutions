"""
LeetCode - 242. Valid Anagram
26.12.2022
"""


s = "anagram"
t = "nagaram"

def isAnagram(s: str, t: str) -> bool:

    s = list(s)
    t = list(t)

    if len(s) != len(t):
        return False

    for letter in t:
        # print(letter)
        if letter in s:
            s.remove(letter)
            # print(s)

    # print(s)
    if not s:
        return True

    return False

print(isAnagram(s,t))