"""
Let N be the number of input equations and M be the number of queries.
Time Complexity: O(M⋅N)
Space Complexity: O(N)
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(defaultdict)
        
        def backtrack(cur, target, acc, visited):
            visited.add(cur)
            ret = -1.0
            nxt = graph[cur]
            if target in nxt:
                ret = acc * nxt[target]
            else:
                for nx, val in nxt.items():
                    if nx in visited:
                        continue
                    ret = backtrack(nx, target, acc*val, visited)
                    if ret != -1.0:
                        break
            visited.remove(cur)
            return ret

        n = len(equations)
        for i in range(n):
            a, b = equations[i]
            graph[a][b] = values[i]
            graph[b][a] = 1/values[i]
        
        ans = []
        for c, d in queries:
            if c not in graph or d not in graph:
                ans.append(-1.0)
            elif c == d:
                ans.append(1.0)
            else:
                visited = set()
                ans.append(backtrack(c, d, 1, visited))
        return ans
