"""
Time complexity : O(nlogn)
Space complexity : O(logN) (or O(n))
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, n):
            a, b = ans[-1]
            x, y = intervals[i]
            if x <= b:
                ans[-1][1] = max(b, y)
            else:
                ans.append([x, y])
        return ans
