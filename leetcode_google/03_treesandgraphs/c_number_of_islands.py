"""DFS
M is the number of rows and N is the number of columns.
Time complexity : O(M×N)
Space complexity : worst case O(M×N) 
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        print(m, n)
        
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    s = [(i, j)]
                    while s:
                        x, y = s.pop()
                        grid[x][y] = '0'
                        for k in range(4):
                            nx = x+dx[k]
                            ny = y+dy[k]
                            if nx<0 or nx>=m or ny<0 or ny>=n:
                                continue
                            if grid[nx][ny] == '1':
                                s.append((nx, ny))
                    ans += 1
                    
        return ans
