"""
Assume that m and n represents the length of l1 and l2 respectively.

Time Complexity: O(max(N, M))

Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode(-1)
        
        cur = ans
        cur1, cur2 = l1, l2
        carry = 0
        while cur1 or cur2:
            if cur1:
                carry += cur1.val
                cur1 = cur1.next
            if cur2:
                carry += cur2.val
                cur2 = cur2.next
            
            cur.next = ListNode(carry%10)
            carry = carry//10
            cur = cur.next
        
        if carry:
            cur.next = ListNode(carry)
        
        return ans.next
