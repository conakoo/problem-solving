"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:
    

Tue Jan  6 23:42:40 KST 2026
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, k = len(haystack), len(needle)
        for i in range(n-k+1):
            if haystack[i:i+k] == needle:
                return i
        return -1
