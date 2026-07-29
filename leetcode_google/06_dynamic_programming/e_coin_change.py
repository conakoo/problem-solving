"""
Time complexity : O(S∗n)
Space complexity : O(S).
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1e9]*(amount+1)
        dp[0] = 0

        for c in coins:
            for x in range(c, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)
        return dp[amount] if dp[amount] != 1e9 else -1
