
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # 1 2 3 4 5 6 7 8 9 0
        # 1->1, 8->8, 0->0
        # 6->9, 9->6
        
        dic = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        
        def fs(k):
            if k == 1:
                return ['0', '1', '8']
            if k == 2:
                return ['00', '11', '69', '88', '96']
            
            ret = []
            nums = fs(k-2)
            for num in nums:
                for k in dic:
                    tmp = k+num+dic[k]
                    ret.append(tmp)
                    
            return ret
        
        ans = fs(n)
        if n>1:
            for num in ans:
                if num[0] == '0':
                    ans.remove(num)
        return ans
