"""
Let N be the number of nodes in the tree.
Time complexity: O(N)
Space complexity: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dbt(x):
            nonlocal ans
            if not x:
                return 0
            l = dbt(x.left)
            r = dbt(x.right)
            ans = max(ans, 1+l+r)
            return max(1+l, 1+r)
        dbt(root)
        return ans-1
