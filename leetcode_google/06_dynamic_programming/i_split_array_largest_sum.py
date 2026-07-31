"""
N is the length of the array and S is the sum of integers in the array.
Time complexity: O(N⋅log(S))
Space complexity: O(1)
"""
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def sa(x): # return how many subarrays need to make x
            cur = 0
            ret = 0 # splits required
            for num in nums:
                if cur+num <= x:
                    cur += num
                else:
                    cur = num
                    ret += 1
            return ret+1
        
        l = max(nums)
        r = sum(nums)
        while l<=r:
            mid = (l+r)//2 # max sum allowed
            if sa(mid) <= k: # number of subarrays to make mid are smaller than k: mid is big
                r = mid-1
                ans = mid
            else:
                l = mid+1
        return ans
