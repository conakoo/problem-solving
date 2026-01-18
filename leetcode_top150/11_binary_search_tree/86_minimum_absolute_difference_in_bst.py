"""LeetCode Top 150
Level:
    Easy
Status:
    Failed
Note:
    

Sun Jan 18 20:45:19 KST 2026
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 1e9
        self.prev = -1e9

        def inorder(x):
            if not x:
                return
            inorder(x.left)
            self.ans = min(self.ans, x.val - self.prev)
            self.prev = x.val
            inorder(x.right)
        
        inorder(root)
        return self.ans
