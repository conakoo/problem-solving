"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:
    

Thu Apr 30 22:48:24 KST 2026
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        n = len(pattern)
        if n != len(s):
            return False

        p2s, s2p = dict(), dict()
        for i in range(n):
            pi, si = pattern[i], s[i]
            if pi not in p2s and si not in s2p:
                p2s[pi], s2p[si] = si, pi
            elif pi not in p2s and si in s2p:
                return False
            elif p2s[pi] != si:
                return False
        return True
