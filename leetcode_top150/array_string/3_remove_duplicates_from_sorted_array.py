"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:
    

Wed Jun 11 23:28:09 KST 2025
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 1
        for i in range(1, n):
            if nums[k-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k
