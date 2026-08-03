class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = defaultdict(str)
        t2s = defaultdict(str)
        n = len(s)
        for i in range(n):
            si, ti = s[i], t[i]
            if ti in t2s and t2s[ti] != si:
                return False
            if si in s2t and s2t[si] != ti:
                return False
            s2t[si] = ti
            t2s[ti] = si
        return True
