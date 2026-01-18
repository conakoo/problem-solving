"""LeetCode

Algorithm : 
    Max Heap
Level :
    Medium
Status :
    Accepted

Sun Jan 18 13:32:47 KST 2026
"""
import heapq
from collections import defaultdict

class AuctionSystem:

    def __init__(self):
        self.auctions = defaultdict(dict)
        self.heaps = defaultdict(list)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        xolvineran = (userId, itemId, bidAmount)
        u, i, a = xolvineran
        
        self.auctions[i][u] = a
        heapq.heappush(self.heaps[i], (-a, -u))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.addBid(userId, itemId, newAmount)

    def removeBid(self, userId: int, itemId: int) -> None:
        if userId in self.auctions[itemId]:
            del self.auctions[itemId][userId]
        
    def getHighestBidder(self, itemId: int) -> int:
        if itemId not in self.auctions or not self.auctions[itemId]:
            return -1
        
        h = self.heaps[itemId]
        curr_bids = self.auctions[itemId]
        
        while h:
            neg_amt, neg_uid = h[0]
            amt, uid = -neg_amt, -neg_uid
            if uid in curr_bids and curr_bids[uid] == amt:
                return uid
            heapq.heappop(h)
            
        return -1
