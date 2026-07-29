class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cnt = defaultdict(int)
        n = len(s)
        for i in range(n):
            cnt[s[i]] += 1
            cnt[t[i]] -= 1
        
        for c in cnt:
            if cnt[c] != 0:
                return False
        return True
