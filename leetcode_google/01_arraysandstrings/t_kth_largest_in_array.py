class Solution:
    # Time Limit Exceeded
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = n-k
        
        def partition(left, right):
            pivot = random.randint(left, right)
            nums[pivot], nums[right] = nums[right], nums[pivot]
            i = left
            for j in range(left, right):
                if nums[j] <= nums[right]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i
        
        def quickselect(left, right):
            if left >= right:
                return
            pivot = partition(left, right)
            
            if pivot == k:
                return
            elif pivot < k:
                quickselect(pivot+1, right)
            else:
                quickselect(left, pivot-1)
        
        quickselect(0, n-1)
        return nums[k]

"""
Given n as the length of nums and m as (maxValue - minValue).
Time complexity: O(n+m)
Space complexity: O(m)
"""
class Solution:
    # Count Sort
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minv, maxv = min(nums), max(nums)
        cnt = [0] * (maxv-minv+1)
        n = len(nums)
        for i in range(n):
            cnt[nums[i]-minv] += 1
        
        tmp = k
        for j in range(len(cnt)-1, -1, -1):
            tmp -= cnt[j]
            if tmp <= 0:
                return j+minv
        return -1
