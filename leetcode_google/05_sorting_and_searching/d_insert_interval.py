"""
Time complexity: O(N)
Space complexity: O(N)
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)//2
            if intervals[mid][0] < newInterval[0]:
                l = mid+1
            else:
                r = mid-1

        intervals.insert(l, newInterval)
        
        ans = []
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
