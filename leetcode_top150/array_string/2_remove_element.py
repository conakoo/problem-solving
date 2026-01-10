"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:
    

Wed Jun 11 23:10:11 KST 2025
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k, p = n, n-1
        for i in range(n):
            while p>0 and nums[p] == val:
                p -= 1
                k -= 1
            if p < i:
                break
            if nums[i] == val:
                nums[i] = nums[p]
                p -= 1
                k -= 1
        
        return k

class Solution2:
    # Focus on elements which are not equal to val
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
