class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        ans = 1
        cnt = defaultdict(int)
        
        n = len(s)
        i, j = 0, 0
        cnt[s[i]] = 1
        while i <= j < n:
            if j == n-1:
                break
            
            while i<n and cnt[s[j+1]] >= 1:
                cnt[s[i]] -= 1
                i += 1
            
            j += 1
            ans = max(ans, j-i+1)
            cnt[s[j]] += 1
        
        return ans
