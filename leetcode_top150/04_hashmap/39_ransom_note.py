"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:
    

Sun Jan 18 21:37:03 KST 2026
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rcnt = [0] * 26
        for c in ransomNote:
            rcnt[ord(c)-ord('a')] += 1

        mcnt = [0] * 26
        for c in magazine:
            mcnt[ord(c)-ord('a')] += 1
        
        for i in range(26):
            if rcnt[i] > mcnt[i]:
                return False
        
        return True

class Solution2:
    # More simple
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = [0] * 26
        for c in magazine:
            cnt[ord(c)-ord('a')] += 1

        for c in ransomNote:
            if cnt[ord(c)-ord('a')] <= 0:
                return False
            cnt[ord(c)-ord('a')] -= 1
        
        return True
