"""LeetCode

Algorithm : 
    Binary Search
Level :
    Medium
Status :
    Failed

Sun Jan 18 13:30:24 KST 2026
"""
class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        n = len(costs)
        combined = [(costs[i], capacity[i]) for i in range(n)]
        combined.sort()

        csts, caps = [], []
        for cst, cap in combined:
            csts.append(cst)
            caps.append(cap)

        dcap = [0] * n
        dcap[0] = caps[0]
        for i in range(1, n):
            dcap[i] = max(dcap[i-1], caps[i])

        l = bisect_left(csts, budget)-1
        ans = dcap[l] if l>=0 else 0

        for i in range(n):
            cst = csts[i]
            if cst >= budget:
                break

            j = bisect_left(csts, budget - cst) - 1
            j = min(j, i - 1)

            if j >= 0:
                ans = max(ans, caps[i]+dcap[j])

        return ans
