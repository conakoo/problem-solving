"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ans = Node(-1)
        
        ori = head
        cur = ans
        tmp = {}
        
        while ori:
            cur.next = Node(ori.val)
            tmp[ori] = cur.next
            cur = cur.next
            ori = ori.next
            
        cur = ans.next
        ori = head
        while ori:
            cur.random = tmp[ori.random] if ori.random else None
            ori = ori.next
            cur = cur.next
        
        return ans.next


class Solution2:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        # A -> A' -> B -> B'
        cur = head
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        
        # random
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        # remove ori
        cur = head.next
        while cur:
            cur.next = cur.next.next if cur.next else None
            cur = cur.next
        
        return head.next
