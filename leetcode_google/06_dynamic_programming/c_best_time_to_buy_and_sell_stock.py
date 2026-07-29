class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        minv = prices[0]
        for i in range(1, n):
            ans = max(ans, prices[i]-minv)
            minv = min(minv, prices[i])
        return ans
