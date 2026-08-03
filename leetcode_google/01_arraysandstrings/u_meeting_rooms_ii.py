"""
Time Complexity: O(NlogN).
Space Complexity: O(N)
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[0])

        pq = [] # store endtime. the len(pq) = rooms
        heapq.heappush(pq, intervals[0][1])
        for start, end in intervals[1:]:
            if pq[0] <= start: # no overlap. update endtime: pop & push
                heapq.heappop(pq)
            heapq.heappush(pq, end)
        return len(pq)
