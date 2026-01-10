"""LeetCode Top 150
Level:
    Medium
Status:
    Accepted
Note:
    

Fri Jun 13 23:08:56 KST 2025
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        n = len(nums)
        for i in range(2, n):
            if nums[k-2] == nums[k-1] == nums[i]:
                continue
            nums[k] = nums[i]
            k += 1
        return k

