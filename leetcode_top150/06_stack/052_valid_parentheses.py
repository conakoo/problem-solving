"""LeetCode Top 150
Level:
    Easy
Status:
    Accepted
Note:
    

Sat Jan 17 22:02:11 KST 2026
"""
class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        p = {')': '(', '}': '{', ']':'['}
        for x in s:
            if x in ['(', '{', '[']:
                st.append(x)
            elif x in p:
                if not st:
                    return False
                if st.pop() != p[x]:
                    return False
        
        return len(st) == 0
