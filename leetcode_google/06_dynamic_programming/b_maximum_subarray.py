class Solution:
    # Time complexity: O(N)
    # Space complexity: O(N)
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        
        return max(dp)

class Solution2:
    # Time complexity: O(N)
    # Space complexity: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = tmp = nums[0]
        for i in range(1, n):
            tmp = max(tmp+nums[i], nums[i])
            ans = max(ans, tmp)
        
        return ans
