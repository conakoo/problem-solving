"""Sliding Window
Level: Medium

Let n be the length of the input array fruits.
Time complexity: O(n)
Space complexity: O(1)
"""
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        
        n = len(fruits)
        cnt = {}
        l = 0

        for r in range(n):
            cnt[fruits[r]] = cnt.get(fruits[r], 0)+1

            while len(cnt) > 2:
                cnt[fruits[l]] -= 1
                if cnt[fruits[l]] == 0:
                    del cnt[fruits[l]]
                l += 1
            
            ans = max(ans, r-l+1)

        return ans
