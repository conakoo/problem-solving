"""Greedy
Level: Medium

Time complexity: O(n)
Space complexity: O(1)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0

        n = len(height)
        i, j = 0, n-1
        while i < j:
            l, r = height[i], height[j]
            h = min(l, r)
            ans = max(ans, h*(j-i))
            if l < r:
                i += 1
            else:
                j -= 1
                
        return ans
