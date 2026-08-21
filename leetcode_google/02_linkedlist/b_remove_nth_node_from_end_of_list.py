"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        l = dummy
        r = dummy
        
        for _ in range(n + 1):
            if not r:
                return head
            r = r.next
        
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return dummy.next
