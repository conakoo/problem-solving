class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = defaultdict(bool)
        for jewel in jewels:
            dic[jewel] = True
        
        ans = 0
        for stone in stones:
            if dic[stone]:
                ans += 1
        
        return ans


class Solution:
    # Better Space Complexity: O(J)
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jset = set(jewels)
        return sum(s in jset for s in stones)
