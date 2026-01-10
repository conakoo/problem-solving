"""LeetCode Top 150
Level:
    Medium
Status:
    Accepted
Note:
    

Sun Aug  3 13:35:51 KST 2025
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        tmp = nums[n-k:]
        for i in range(n-1, k-1, -1):
            nums[i] = nums[i-k]
        for i in range(k):
            nums[i] = tmp[i]

class Solution2:
    # More simple
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[k:], nums[:k] = nums[:n-k], nums[n-k:]
