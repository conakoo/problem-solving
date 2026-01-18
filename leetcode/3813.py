"""LeetCode

Algorithm : 
    String
Level :
    Easy
Status :
    Accepted

Sun Jan 18 13:31:28 KST 2026
"""
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v, c = 0, 0
        
        for x in s:
            if x in ['a', 'e', 'i', 'o', 'u']:
                v += 1
            elif ord('a') < ord(x) <= ord('z'):
                c += 1

        return floor(float(v)/float(c)) if c!=0 else 0
            