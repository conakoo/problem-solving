"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:
    

Sat Jan 10 23:13:07 KST 2026
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        tmp = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        ans = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == 'I' and i<n-1 and s[i+1] == 'V':
                ans += 4
                i += 2
            elif s[i] == 'I' and i<n-1 and s[i+1] == 'X':
                ans += 9
                i += 2
            elif s[i] == 'X' and i<n-1 and s[i+1] == 'L':
                ans += 40
                i += 2
            elif s[i] == 'X' and i<n-1 and s[i+1] == 'C':
                ans += 90
                i += 2
            elif s[i] == 'C' and i<n-1 and s[i+1] == 'D':
                ans += 400
                i += 2
            elif s[i] == 'C' and i<n-1 and s[i+1] == 'M':
                ans += 900
                i += 2
            else:
                ans += tmp[s[i]]
                i += 1

        return ans

class Solution2:
    def romanToInt(self, s: str) -> int:
        tmp = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        ans = 0
        n = len(s)
        for i in range(n-1):
            si, sii = s[i], s[i+1]
            if tmp[si] < tmp[sii]:
                ans -= tmp[si]
            else:
                ans += tmp[si]

        return ans + tmp[s[-1]]
