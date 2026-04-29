"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:
    

Wed Apr 29 21:19:05 KST 2026
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = j = 0
        ns, nt = len(s), len(t)

        while True:
            if i >= ns:
                return True
            if j >= nt:
                break

            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        return False

class Solution2:
    # More shorter code
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp = 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        
        return sp == len(s)
