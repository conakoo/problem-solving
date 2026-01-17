"""LeetCode Top 150
Level:
    Medium
Status:
    Accepted
Note:
    

Sat Jan 17 22:39:12 KST 2026
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                x = s.pop()
                y = s.pop()
                s.append(int(eval(f"{y} {token} {x}")))
            else:
                s.append(int(token))
        return s[0]
