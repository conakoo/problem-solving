"""
Let N be the number of nodes in the smaller tree.
Time Complexity: O(N).
Space Complexity: O(N).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def fe(x, y):
            if not x and not y:
                return True
            elif not x or not y:
                return False
            
            if (
                x.val == y.val
                and (
                    (fe(x.left, y.left) and fe(x.right, y.right))
                    or (fe(x.left, y.right) and fe(x.right, y.left))
                )
            ):
                return True
            else:
                return False
        
        return fe(root1, root2)
