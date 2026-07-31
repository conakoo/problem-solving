"""
Time complexity : O(n^2)
Space complexity : O(n)
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            for j in range(1, nums[i]+1):
                if dp[min(n-1, i+j)]:
                    dp[i] = True
                    break
        return dp[0]
