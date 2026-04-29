"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:

Regular Expressions (Regex) define search patterns.
.  = any character | \d = digit      | \w    = word char      | \s = whitespace
*  = 0+ repeats    | +  = 1+ repeats | ?     = 0 or 1
^  = start         | $  = end        | [abc] = set of chars
Example: r'\d{3}-\d{4}' matches a phone number pattern like 123-4567.
Example: r'[^a-zA-Z0-9]' ^ means not. matches not a letter or a number

Wed Apr 29 20:59:25 KST 2026
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        tmp = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return tmp == tmp[::-1]
