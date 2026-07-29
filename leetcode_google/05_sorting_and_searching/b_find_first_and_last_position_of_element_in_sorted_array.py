class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n-1
        
        tmp = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                tmp = mid
                break
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        
        if tmp == -1:
            return [-1, -1]
        start, end = tmp, tmp
        while start>=0 and nums[start]==target:
            start -= 1
        while end<n and nums[end]==target:
            end += 1
        
        start, end = start+1, end-1
        return [start, end]
