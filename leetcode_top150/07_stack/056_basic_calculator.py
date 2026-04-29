"""LeetCode Top 150
Level:
    Hard
Status:
    Failed
Note:
    Use one stack(st) to store sign and one variable(num) for number

Sat Jan 17 21:55:06 KST 2026
"""
class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        num = 0
        sign = 1
        st = [sign]
        
        for x in s:
            if x.isdigit():
                num = 10*num + int(x)
            elif x == '(':
                st.append(sign)
            elif x == ')':
                st.pop()
            elif x == '+' or x == '-':
                ans += sign * num
                sign = (1 if x == '+' else -1) * st[-1]
                num = 0
        return ans + sign * num
