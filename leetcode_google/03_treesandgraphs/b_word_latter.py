"""
M is the length of each word and N is the total number of words in the input word list.
Time Complexity: O(M^2 × N)
Space Complexity: O(M^2 × N)
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (
            endWord not in wordList
            or not endWord
            or not beginWord
            or not wordList
        ):
            return 0
        
        l = len(beginWord)
        h = defaultdict(list) # 'a*b'->['acb']
        for w in wordList:
            for i in range(l):
                tmp = w[:i]+'*'+w[i+1:]
                h[tmp].append(w)
        
        from collections import deque
        q = deque([(beginWord, 1)])
        visited = {beginWord: True}
        while q:
            cur, level = q.popleft()
            visited[cur] = True
            for i in range(l):
                tmp = cur[:i]+'*'+cur[i+1:]
                for w in h[tmp]:
                    if w == endWord:
                        return level+1
                    if w not in visited:
                        q.append((w, level+1))
                h[tmp] = [] # to ignore loop
        return 0
