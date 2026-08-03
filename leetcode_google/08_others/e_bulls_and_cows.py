class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b, c = 0, 0
        
        n = len(secret)
        cnt = defaultdict(int)
        for i in range(n):
            si, gi = secret[i], guess[i]
            if si == gi:
                b += 1
            else:
                cnt[si] += 1
        print(cnt)
        
        for i in range(n):
            si, gi = secret[i], guess[i]
            if si!=gi and cnt[gi]:
                c += 1
                cnt[gi] -= 1
        return str(b)+'A'+str(c)+'B'


class Solution2:
    # Better
    def getHint(self, secret: str, guess: str) -> str:
        cnt = defaultdict(int) # cnt[s]: in s not g, cnt[g]: in g not s
        b = c = 0
        n = len(secret)
        for i in range(n):
            si, gi = secret[i], guess[i]
            if si == gi:
                b += 1
            else:
                c += int(cnt[si]<0) # in s < in g
                c += int(cnt[gi]>0) # in s > in g
                cnt[si] += 1
                cnt[gi] -= 1
        return f"{b}A{c}B"
