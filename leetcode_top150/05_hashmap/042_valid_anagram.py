"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:
    

Thu Apr 30 22:52:18 KST 2026
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False

        cnt = [0]*26
        for i in range(n):
            cnt[ord(s[i])-ord('a')] += 1
            cnt[ord(t[i])-ord('a')] -= 1
        
        return all(x == 0 for x in cnt)
