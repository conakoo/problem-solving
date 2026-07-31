# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = ''
        if not root:
            return ans
        
        from collections import deque
        q = deque([root])
        while q:
            cur = q.popleft()
            if not cur:
                ans += 'None,'
                continue
            ans += str(cur.val) + ','
            q.append(cur.left)
            q.append(cur.right)
        return ans # store all 'parent, left, right, ...'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        ls = data.split(',')
        root = TreeNode(int(ls[0]))
        from collections import deque
        q = deque([root]) # track node
        i = 1
        while q and i < len(ls):
            cur = q.popleft()
            if ls[i] != 'None':
                left = TreeNode(int(ls[i]))
                cur.left = left
                q.append(left)
            i += 1
            if ls[i] != 'None':
                right = TreeNode(int(ls[i]))
                cur.right = right
                q.append(right)
            i += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
