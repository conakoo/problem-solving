"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:
    

Thu Apr 30 22:41:52 KST 2026
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        s2t, t2s = dict(), dict()
        for i in range(n):
            si, ti = s[i], t[i]
            if si not in s2t and ti not in t2s:
                s2t[si], t2s[ti] = ti, si
            elif si not in s2t and ti in t2s:
                return False
            elif ti != s2t[si]:
                return False
        return True
