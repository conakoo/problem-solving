"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:
    

Sat Jan 10 23:35:54 KST 2026
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        ans = ''
        for i in range(201):
            if i >= len(strs[0]):
                return ans
            c = strs[0][i]
            is_common = True
            for s in strs:
                if i >= len(s):
                    return ans
                if c != s[i]:
                    is_common = False
                    break
            if not is_common:
                return ans
            ans += c
        return ans
