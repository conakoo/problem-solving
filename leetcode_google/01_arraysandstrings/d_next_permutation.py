"""Two Pointers
Level: Medium
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        def swap(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        i = n-2
        while 0<=i and nums[i+1]<=nums[i]: # find when is first decreasing element from right
            i -= 1
        if i>=0:
            j = n-1
            while nums[j]<=nums[i]: # find when is first larger element
                j -= 1
            swap(nums, i, j)
        nums[i+1:] = reversed(nums[i+1:])
