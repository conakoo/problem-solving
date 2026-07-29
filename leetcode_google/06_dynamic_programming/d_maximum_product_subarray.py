"""
Time complexity : O(N)
Space complexity : O(1)
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = minv = maxv = nums[0]

        for i in range(1, n):
            cur = nums[i]
            tmp = max(cur, max(maxv*cur, minv*cur))
            minv = min(cur, min(maxv*cur, minv*cur))
            maxv = tmp
            ans = max(ans, maxv)

        return ans
