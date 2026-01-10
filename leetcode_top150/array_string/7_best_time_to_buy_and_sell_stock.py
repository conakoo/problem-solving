"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:
    

Sun Aug  3 13:49:15 KST 2025
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ans = 0
        n = len(prices)
        tmp = prices[0]
        for i in range(1, n):
            ans = max(ans, prices[i]-tmp)
            tmp = min(tmp, prices[i])
        return ans
