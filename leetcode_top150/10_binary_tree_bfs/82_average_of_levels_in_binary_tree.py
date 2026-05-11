"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:
    

Mon May 11 23:51:18 KST 2026
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        tmp = []
        cnt = []

        from collections import deque
        q = deque([(0, root)])

        while q:
            level, cur = q.popleft()
            if len(tmp) <= level:
                tmp.append(cur.val)
                cnt.append(1)
            else:
                tmp[level] += cur.val
                cnt[level] += 1
            
            if cur.left:
                q.append((level+1, cur.left))
            if cur.right:
                q.append((level+1, cur.right))

        ans = [tmp[i]/cnt[i] for i in range(len(tmp))]
        return ans

class Solution:
    # Retrieve number of nodes in that level during search -> Smaller space
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        ans = []

        from collections import deque
        q = deque([root])

        while q:
            size = len(q)
            tmp = 0

            for _ in range(size):
                cur = q.popleft()
                tmp += cur.val
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans.append(tmp/size)

        return ans
