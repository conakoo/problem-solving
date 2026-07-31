class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_END = '#'
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {}) # return value if c in node else set node[c]={}
            node[WORD_END] = word
        
        n, m = len(board), len(board[0])
        ans = []

        def fw(x, y, parent):
            c = board[x][y]
            cur = parent[c]
            word = cur.pop(WORD_END, False) # pop word if WORD_END in cur else False
            if word:
                ans.append(word)
            
            board[x][y] = '#' # mark visted

            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if not board[nx][ny] in cur: # not match
                    continue
                fw(nx, ny, cur)
            
            board[x][y] = c # restore
            if not cur: # remove the leaf
                parent.pop(c)


        for i in range(n):
            for j in range(m):
                if board[i][j] in trie:
                    fw(i, j, trie)

        return ans
