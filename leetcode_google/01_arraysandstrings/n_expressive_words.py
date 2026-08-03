class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def count_char(string):
            ret = []
            prev, tmp = string[0], 1
            for c in string[1:]:
                if prev == c:
                    tmp += 1
                else:
                    ret.append((prev, tmp))
                    prev = c
                    tmp = 1
            ret.append((prev, tmp))
            return ret # list of (char, count)
        
        ans = 0
        cnt_s = count_char(s)
        for word in words:
            cnt_w = count_char(word)
            if len(cnt_s) != len(cnt_w):
                continue
            is_stretchy = True
            for i in range(len(cnt_s)):
                if cnt_s[i][0] != cnt_w[i][0]:
                    is_stretchy = False
                    break
                if cnt_w[i][1] > cnt_s[i][1]:
                    is_stretchy = False
                    break
                if cnt_s[i][1]!=cnt_w[i][1] and cnt_s[i][1]<3:
                    is_stretchy = False
                    break
            ans = ans+1 if is_stretchy else ans
        return ans
        
        
            