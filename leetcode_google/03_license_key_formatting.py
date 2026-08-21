"""String
Level: Easy
"""
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = s.replace("-", "").upper()
        n = len(chars)
        
        ans = ""
        index = 0
        if n%k != 0:
            ans += chars[:n%k] + "-"
            index = n%k
        
        while index < n:
            ans += chars[index:index+k] + "-"
            index = index+k
        return ans[:-1]
