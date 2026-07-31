class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        ans = [0]*(n1+n2)
        for j in range(n2):
            carry = 0
            for i in range(n1):
                tmp = int(num1[n1-1-i])*int(num2[n2-1-j])
                ans[i+j] += tmp
        
        carry = 0
        for i in range(n1+n2):
            tmp = ans[i]+carry
            carry = tmp//10
            ans[i] = str(tmp%10)
            
        ans = "".join(ans)[::-1]
        for i in range(n1+n2):
            if ans[i]!='0':
                return ans[i:]
        
        return "0"
                