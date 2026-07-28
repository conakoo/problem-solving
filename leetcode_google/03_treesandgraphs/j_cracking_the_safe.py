"""
Time Complexity: O(n ∗ k^n)
Space Complexity: O(n ∗ k^n)
"""
class Solution:
    # Find Euler Path (a path visiting every edge exactly once) = Hierholzer's Algorithm
    #           01
    #     0 --------> 1
    #     ↑           |
    #  00 |           | 11
    #     |           ↓
    #     0 <-------- 1
    #           10
    def crackSafe(self, n: int, k: int) -> str:
        seen = set() # store edge not node
        ans = []

        def dfs(x):
            for i in range(k):
                nx = x + str(i)
                if nx not in seen:
                    seen.add(nx)
                    dfs(nx[1:])
                    ans.append(str(i))
        
        dfs('0'*(n-1))
        return ''.join(ans) + '0'*(n-1)
