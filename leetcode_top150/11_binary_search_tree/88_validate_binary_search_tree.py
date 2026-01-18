"""LeetCode Top 150
Level:
    Medium
Status:
    Accepted
Note:
    

Sun Jan 18 21:04:03 KST 2026
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid(cur, min, max):
            if not cur:
                return True
            
            if cur.val <= min or cur.val >= max:
                return False
            
            left = is_valid(cur.left, min, cur.val)
            right = is_valid(cur.right, cur.val, max)
            return left and right
        
        return is_valid(root, -3e9, 3e9)
