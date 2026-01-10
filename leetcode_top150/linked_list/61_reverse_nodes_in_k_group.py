"""LeetCode Top 150
Level:
    Hard
Status:
    Accepted
Note:
    

Sat Jan 10 22:37:21 KST 2026
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        x = ListNode(0)
        x.next = head
        prev = x
        
        cur = head
        tmp = []

        while cur:
            tmp.append(cur)
            cur = cur.next
            
            if len(tmp) == k:
                for i in range(k-1, 0, -1):
                    tmp[i].next = tmp[i-1] 
                prev.next = tmp[k-1]
                tmp[0].next = cur
                prev = tmp[0]
                tmp = []

        return x.next

class Solution2:
    # TODO: Apply Recursive Pattern -> Space: O(1)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return
