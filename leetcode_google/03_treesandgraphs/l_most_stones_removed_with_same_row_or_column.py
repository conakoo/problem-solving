"""
Let n be the length of the stones array.
Time complexity: O(n^2)
Space complexity: O(n^2)
"""
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = stones[i]
                x2, y2 = stones[j]
                if x1 == x2 or y1==y2:
                    adj[i].append(j)
                    adj[j].append(i)
        
        connected = 0
        visited = [False]*n

        def dfs(x):
            visited[x] = True
            for nx in adj[x]:
                if not visited[nx]:
                    dfs(nx)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                connected += 1
        
        return n - connected
