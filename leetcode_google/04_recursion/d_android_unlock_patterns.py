class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        
        visited = [[False]*3 for _ in range(3)]
        
        ans = 0
        def nop(x, y, k):
            nonlocal ans
            if k > n:
                return

            visited[x][y] = True
            if m <= k <= n:
                ans += 1
            
            dx = [-1, -1, -1, 0, 1, 1, 1, 0, -2, -2, 1, -1, 2, 2, -1, 1]
            dy = [-1, 0, 1, 1, 1, 0, -1, -1, -1, 1, 2, 2, 1, -1, -2, -2]

            skipx = [0, 0, 2, -2, -2, 2, 2, -2]
            skipy = [2, -2, 0, 0, -2, 2, -2, 2]
            for i in range(16):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or nx>=3 or ny<0 or ny>=3:
                    continue
                if not visited[nx][ny]:
                    nop(nx, ny, k+1)
            
            for i in range(8):
                nx = x+skipx[i]
                ny = y+skipy[i]
                if nx<0 or nx>=3 or ny<0 or ny>=3:
                    continue
                if not visited[nx][ny]:
                    midx = (x+nx)//2
                    midy = (y+ny)//2
                    if visited[midx][midy]:
                        nop(nx, ny, k+1)
            
            visited[x][y] = False
        
        for i in range(3):
            for j in range(3):
                nop(i, j, 1)
        return ans
