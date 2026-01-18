"""LeetCode Top 150
Level:
    Medium
Status:
    Accepted
Note:
    Inorder traversal travels from left to right.
    Finding kth smallest value means the time when visits node.

Sun Jan 18 20:49:26 KST 2026
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.tmp = []

        def traverse(cur):
            if not cur:
                return
            traverse(cur.left)
            self.tmp.append(cur.val)
            traverse(cur.right)
        
        traverse(root)
        self.tmp.sort()
        return self.tmp[k-1]

class Solution2:
    # Use inorder traversal and less space
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.ans = None

        def inorder(cur):
            if not cur:
                return
            inorder(cur.left)
            self.cnt += 1
            if self.cnt == k:
                self.ans = cur.val
                return
            inorder(cur.right)

        inorder(root)
        return self.ans
