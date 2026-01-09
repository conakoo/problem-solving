"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:
    

Fri Jan  9 22:50:44 KST 2026
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        is_char = False
        
        ans = 0
        for i in range(n-1, -1, -1):
            if s[i] != ' ':
                is_char = True
                ans += 1
            elif is_char and s[i] == ' ':
                return ans
        return ans
    
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        return len(words[-1])
