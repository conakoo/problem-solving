"""
V represents the number of vertices and E represents the number of edges.
Time Complexity: O(V+E)
Space Complexity: O(V+E)
"""
class Solution:
    # Topological Sort = Kahn's Algorithm
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        from collections import deque
        q = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        ans = []
        while q:
            x = q.popleft()
            ans.append(x)
            for nx in graph[x]:
                indegree[nx] -= 1
                if indegree[nx] == 0:
                    q.append(nx)
                    
        if indegree.count(0) != numCourses:
            return []
        return ans
