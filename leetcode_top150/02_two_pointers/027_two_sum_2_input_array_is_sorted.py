"""LeetCode Top 150
Level:
    Medium
Status:
    Accepted
Note:
    

Wed Apr 29 21:25:22 KST 2026
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1
        while i < j:
            if numbers[i]+numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i]+numbers[j] < target:
                i += 1
            else:
                j -= 1
