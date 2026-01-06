"""LeetCode Top 150
Level:
    Hard
Status:
    Failed
Note:
    

Tue Jan  6 23:36:45 KST 2026
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        tmp = [1] * n

        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                tmp[i] = tmp[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                tmp[i] = max(tmp[i], tmp[i+1]+1)
        
        return sum(tmp)
