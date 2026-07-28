"""
Time Complexity: O(N+M)

Space Complexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-200)
        cur = ans
        
        cur1, cur2 = list1, list2
        while cur1 or cur2:
            tmp = 100
            if cur1:
                tmp = min(tmp, cur1.val)
            if cur2:
                tmp = min(tmp, cur2.val)
            
            while cur1 and cur1.val == tmp:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            while cur2 and cur2.val == tmp:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next
        
        return ans.next
