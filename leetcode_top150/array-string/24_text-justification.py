"""LeetCode Top 150
Level:
    Hard
Status:
    Accepted
Note:
    

Fri Jan  9 23:47:35 KST 2026
"""
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        n = len(words)

        tmp, tmp_w = [words[0]], len(words[0])
        for i in range(1, n):
            w = len(words[i])
            if tmp_w + len(tmp) + w <= maxWidth:
                tmp.append(words[i])
                tmp_w += w
                continue
            else:
                
                n_space = maxWidth - tmp_w
                ns = max(len(tmp)-1, 1)
                s, r = n_space//ns, n_space % ns

                line = ""
                for idx in range(len(tmp)):
                    line += tmp[idx]
                    if r > 0:
                        line += " " * (s + 1)
                        n_space -= s+1
                        r -= 1
                    else:
                        line += " " * min(s, n_space)
                        n_space -= s
                    
                ans.append(line)
                tmp, tmp_w = [words[i]], w
        
        line = " ".join(tmp)
        line += " "*(maxWidth - tmp_w - len(tmp)+1)
        ans.append(line)

        return ans
            