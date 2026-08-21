"""Array
Level: Easy
"""
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []
        
        if not nums:
            ans.append([lower, upper])
            return ans

        nums = [lower]+nums+[upper]
        n = len(nums)
        prev = nums[0]
        for i in range(1, n):
            if i == 1 and prev!=nums[i]:
                ans.append([prev, nums[i]-1])
            elif i == n-1 and prev!=nums[i]:
                ans.append([prev+1, nums[i]])
            elif prev+1 < nums[i]:
                ans.append([prev+1, nums[i]-1])
            prev = nums[i]
        
        return ans
