class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        ans = []
        n = len(digits)
        def lc(x, prefix=''):
            nonlocal ans
            if x == n-1:
                ans.append(prefix)
                return
            d = digits[x+1]
            for nxt in dic[d]:
                lc(x+1, prefix+nxt)
        
        for d in dic[digits[0]]:
            lc(0, prefix=d)
        
        return ans
