class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        lm, rm = height[l], height[r]

        ans = 0
        while l <= r:
            lm = max(lm, height[l])
            rm = max(rm, height[r])

            if lm < rm:
                ans += lm - height[l]
                l += 1
            else:
                ans += rm - height[r]
                r -= 1
        
        return ans
