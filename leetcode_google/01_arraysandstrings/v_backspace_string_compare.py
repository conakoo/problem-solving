class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def apply_backspace(string):
            tmp = []
            for c in string:
                if c == '#':
                    if tmp: tmp.pop()
                else:
                    tmp.append(c)
            return tmp
        tmp_s, tmp_t = apply_backspace(s), apply_backspace(t)
        print(tmp_s, tmp_t)
        
        return tmp_s == tmp_t
    
class Solution2:
    # Better space complexity: O(N) -> O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        def nxt(string, idx):
            nb = 1
            while idx>=0 and nb != 0:
                if string[idx] == '#':
                    nb += 1
                else:
                    nb -= 1
                idx -= 1
            return idx
        
        ns, nt = len(s), len(t)
        i, j = ns-1, nt-1
        
        while True:
            while i!=-1 and s[i] == '#':
                i = nxt(s, i-1)
            while j!=-1 and t[j] == '#':
                j = nxt(t, j-1)
                
            if i<0 or j<0:
                break
            if s[i] != t[j]:
                return False
            i -= 1
            j -= 1
        
        return i == j


class Solution3:
    # Better readibility
    def backspaceCompare(self, s: str, t: str) -> bool:
        def nxt(string, idx):
            nb = 0
            while idx >= 0:
                if string[idx] == '#':
                    nb += 1
                    idx -= 1
                elif nb > 0:
                    nb -= 1
                    idx -= 1
                else:
                    break
            return idx
        
        i, j = len(s)-1, len(t)-1
        
        while i >= 0 or j >= 0:
            i = nxt(s, i)
            j = nxt(t, j)
            
            if i < 0 or j < 0:
                return i == j
            
            if s[i] != t[j]:
                return False
                
            i -= 1
            j -= 1
            
        return True
