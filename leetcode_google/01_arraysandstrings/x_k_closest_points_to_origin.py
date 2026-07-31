
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = defaultdict(list) # distance -> point
        for x, y in points:
            d = x**2 + y**2
            dist[d].append([x, y])
        
        keys = sorted(dist.keys())
        
        ans = []
        for key in keys:
            for point in dist[key]:
                ans.append(point)
                if len(ans) == k:
                    return ans

class Solution:
    # Better Complexity:
    #   Time Complexity: O(N)
    #   Space Complexity: O(1)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(point):
            return point[0] ** 2 + point[1] ** 2
        
        def partition(left, right):
            d = distance(points[right])
            i = left

            for j in range(left, right):
                if distance(points[j]) <= d:
                    points[i], points[j] = points[j], points[i]
                    i += 1

            points[i], points[right] = points[right], points[i]
            return i

        def quickselect(left, right):
            if left >= right:
                return

            pivot = partition(left, right)

            if pivot == k:
                return
            elif pivot < k:
                quickselect(pivot + 1, right)
            else:
                quickselect(left, pivot - 1)

        n = len(points)
        quickselect(0, n-1)
        return points[:k]
