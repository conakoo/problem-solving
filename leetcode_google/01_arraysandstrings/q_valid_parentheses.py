class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', '}': '{', ']': '['}
        st = []
        for c in s:
            if c in dic and st and st[-1] != dic[c]:
                return False
            elif c in dic and st and st[-1] == dic[c]:
                st.pop()
            else:
                st.append(c)
        return len(st) == 0
