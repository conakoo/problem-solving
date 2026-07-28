"""
Time complexity : O(mn)
Space complexity : O(mn)
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        dp = [[0]*n for _ in range(m)]

        def dfs(x, y):
            if dp[x][y]!=0:
                return dp[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or nx>=m or ny<0 or ny>=n:
                    continue
                if matrix[x][y] < matrix[nx][ny]:
                    dp[x][y] = max(dp[x][y], dfs(nx, ny))
            dp[x][y] += 1
            return dp[x][y]
            
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans
        