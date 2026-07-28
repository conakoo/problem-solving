"""
Time complexity: O(n)

Space complexity: O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -1e9
        
        def mps(x):
            if not x:
                return 0
            
            l = max(mps(x.left), 0)
            r = max(mps(x.right), 0)
            self.ans = max(self.ans, x.val+l+r)
            return x.val + max(l, r)
        
        mps(root)
        return self.ans
    

class Solution2:
    # nonlocal
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float("inf")

        def mps(x) -> int:
            nonlocal ans
            if not x:
                return 0
            l = max(mps(x.left), 0)
            r = max(mps(x.right), 0)
            ans = max(ans, x.val+l+r)
            return max(x.val+l, x.val+r)
        mps(root)
        return ans
