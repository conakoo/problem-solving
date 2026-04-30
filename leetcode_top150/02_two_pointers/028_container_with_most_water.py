"""LeetCode Top 150
Level:
    Medium
Status:
    Failed
Note:
    

Thu Apr 30 22:30:09 KST 2026
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        ans = 0
        i, j = 0, n-1
        while i < j:
            tmp = min(height[i], height[j])*(j-i)
            ans = max(ans, tmp)
            
            # need to keep max area so find bigger height
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans
