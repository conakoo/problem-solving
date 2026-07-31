class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        seats = [1]+seats+[1]
        n = len(seats)
        
        ans = 0
        l, r = 0, 1
        while l < r < n:
            if r==n-1:
                ans = max(ans, r-l-1)
                break
            elif seats[r] == 1:
                ans = max(ans, (r-l)//2)
                if l == 0:
                    ans = max(ans, r-l-1)
                l = r
                r = l+1
            else:
                r += 1
        return ans
