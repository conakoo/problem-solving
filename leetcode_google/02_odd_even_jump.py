class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # monotonic stack: a specialized stack data structure that enforces a strict ordering rule 
        # where elements from bottom to top are always sorted in either strictly increasing or decreasing order
        def make(indexes):
            ans = [None] * n
            s = []
            for i in indexes:
                # 스택의 맨 위(stack[-1])에 있는 인덱스의 값보다, 현재 인덱스 i의 값이 더 크다면?
                # 바로 이것이! 스택에 들어있던 그 인덱스 입장에서 "나보다 값이 크면서, 정렬된 순서상 가장 먼저 나타나는(즉, 조건에 딱 맞는) 다음 인덱스"를 찾은 것입니다!
                while s and i > s[-1]:
                    ans[s.pop()] = i
                s.append(i)
            return ans
        
        tmp = sorted(range(n), key=lambda x: arr[x]) # arr value가 작은 인덱스부터 큰 인덱스 순서로 줄을 세워놓은 리스트
        oddnext = make(tmp)
        tmp.sort(key= lambda x: -arr[x])
        evennext = make(tmp)

        odd = [None] * n
        even = [None] * n
        odd[n-1] = even[n-1] = True

        for i in range(n-2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]
        
        return sum(odd)
