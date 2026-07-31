class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gp(k):
            if k == 0:
                return ['']
            ret = []
            for i in range(k):
                left = gp(i)
                right = gp(k-1-i)
                for l in left:
                    for r in right:
                        ret.append('('+l+')'+r)
            return ret
        
        return gp(n)


class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def gp(parenthesis, l, r):
            if len(parenthesis) == 2*n:
                ans.append(parenthesis)
            if l<n:
                gp(parenthesis+'(', l+1, r)
            if r<l:
                gp(parenthesis+')', l, r+1)
        
        gp('', 0, 0)
        return ans
