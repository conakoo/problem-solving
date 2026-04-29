"""LeetCode Top 150
Level:
    Medium
Status:
    Accepted
Note:
    

Sat Jan 17 22:15:35 KST 2026
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        tmp = path.split('/')
        n = len(tmp)

        ans = []
        for i in range(n):
            if tmp[i] == '':
                continue
            elif tmp[i] == '.':
                continue
            elif tmp[i] == '..':
                if ans:
                    ans.pop()
            else:
                ans.append(tmp[i])
        
        return '/' + '/'.join(ans)
