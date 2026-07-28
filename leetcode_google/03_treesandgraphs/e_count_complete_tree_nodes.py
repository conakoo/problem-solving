# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return 0
        
        from collections import deque
        q = deque([root])
        while q:
            cur = q.popleft()
            ans += 1
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
        
        return ans
