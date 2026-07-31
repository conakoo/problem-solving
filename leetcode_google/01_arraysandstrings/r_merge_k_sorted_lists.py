"""
k is the number of linked lists.
Time complexity : O(Nlogk)
Space complexity :
    O(n)
    O(k)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        pq = []
        for i in range(len(lists)):
            if lists[i]: 
                heapq.heappush(pq, (lists[i].val, i, lists[i]))
        
        head = ListNode(-1e9)
        cur = head
        while pq:
            x, idx, ptr = heapq.heappop(pq)
            while ptr and ptr.val == x:
                cur.next = ptr
                ptr = ptr.next
                cur = cur.next
            if ptr:
                heapq.heappush(pq, (ptr.val, idx, ptr))
        
        return head.next


class Solution:
    # Better Space Capacity: O(1)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(x, y):
            head = cur = ListNode(-1)
            while x and y:
                if x.val <= y.val:
                    cur.next = x
                    x = x.next
                else:
                    cur.next = y
                    y = x
                    x = cur.next.next
                cur = cur.next
            if not x:
                cur.next = y
            else:
                cur.next = x
            return head.next

        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0, n-interval, interval*2):
                lists[i] = merge2Lists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if n>0 else None
