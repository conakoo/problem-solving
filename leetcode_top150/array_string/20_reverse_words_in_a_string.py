"""LeetCode Top 150
Level:
    Medium
Status:
    Accepted
Note:
    

Fri Jan  9 22:55:46 KST 2026
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        ans = ' '.join(words[::-1])
        return ans
