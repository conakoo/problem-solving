"""
N is the number of input words and L is the length of a single word.
Time complexity: O(N x 26^L)
Space Complexity: O(N⋅L)
"""
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        dic = defaultdict(set) # prefix -> [word]
        for word in words:
            for prefix in (word[:i] for i in range(1, len(word))):
                dic[prefix].add(word)
        
        n = len(words[0])
        ans = []
        def wc(k, cur):
            if k == n:
                ans.append(cur[:])
                return
            prefix = ''.join([c[k] for c in cur])
            for nxt in dic[prefix]:
                cur.append(nxt)
                wc(k+1, cur)
                cur.pop()
        
        for word in words:
            cur = [word]
            wc(1, cur)
        return ans
