class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        rev = digits[::-1]
        carry = 1
        for i in range(n):
            tmp = rev[i]
            rev[i] = (tmp+carry) % 10
            carry = (tmp+carry) // 10
        if carry:
            rev.append(carry)
        return rev[::-1]
