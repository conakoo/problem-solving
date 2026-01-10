"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:
    

Fri Jun 13 23:23:36 KST 2025
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        from collections import defaultdict
        cnt = defaultdict(int)
        for i in range(n):
            cnt[nums[i]] += 1
            if cnt[nums[i]] > n//2:
                return nums[i]

class Solution:
    # Boyer-Moore Majority Vote algorithm -> Space: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        ans = cnt = 0
        for x in nums:
            if cnt == 0:
                ans = x
            
            if x == ans:
                cnt += 1
            else:
                cnt -= 1
        return ans
