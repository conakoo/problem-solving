class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for c in s:
            if c == ']':
                tmp = []
                while st[-1] != '[':
                    tmp.append(st.pop())
                st.pop() # remove [
                b, k = 1, 0
                while st and st[-1].isdigit():
                    k += int(st.pop())*b
                    b*=10
                st.append(k*''.join(reversed(tmp)))
            else:
                st.append(c)
        return "".join(st)
