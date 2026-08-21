# O(1) < O(log N) < O(N) < O(N log N) < O(N²) < O(N³) < O(2N) < O(N!)

# 자료구조	접근	탐색	삽입	삭제	비고
# 배열 / 동적배열	O(1)	O(N)	O(N)	O(N)	끝에 append는 상환 O(1)
# 연결 리스트	O(N)	O(N)	O(1)*	O(1)*	*노드 포인터를 이미 알 때
# 스택 / 큐 / 덱	—	—	O(1)	O(1)	덱은 양쪽 다 O(1)
# 해시 테이블	—	O(1)	O(1)	O(1)	최악 O(N) (충돌 몰림)
# 이진 탐색 트리(균형)	O(log N)	O(log N)	O(log N)	O(log N)	불균형 시 O(N)
# 힙 (이진)	O(1) 최상단	O(N)	O(log N)	O(log N)	임의 원소 탐색은 느림
# Union-Find	—	≈O(1)	≈O(1)	—	경로압축+랭크 시 α(N)
# Trie	O(L)	O(L)	O(L)	O(L)	L = 문자열 길이

class TwoPointer:
    """
    양끝 또는 같은 방향 두 인덱스를 움직여 O(N²) 이중 루프를 O(N)으로 줄인다
    * two_sum_sorted: 정렬된 배열에서 합이 target인 쌍 찾기
    """
    def two_sum_sorted(arr, target):
        n = len(arr)
        l, r = 0, n-1
        while l < r:
            tmp = arr[l] + arr[r]
            if tmp == target:
                return (l, r)
            elif tmp < target:
                l += 1
            else:
                h -= 1
        return None


class SlidingWindow:
    """
    연속 부분 구간 문제. 오른쪽으로 확장하고 조건 위반 시 왼쪽을 줄인다
    * max_sum_k: 길이 k 구간의 최대 합 -- fixed window size
    * min_window_sum: 합이 target 이상인 가장 짧은 연속 구간 -- dynamic window size
    """
    def max_sum_k(arr, k):
        cur = sum(arr[:k])
        ans = cur
        for i in range(k, len(a)):
            cur += arr[i] - arr[i - k]
            ans = max(ans, cur)
        return ans

    def min_window_sum(arr, target):
        n = len(arr)
        l = r = 0
        tmp = 0
        ans = 1e9
        while r < n:
            tmp += arr[r]
            while tmp >= target:
                ans = min(ans, r-l+1)
                tmp -= arr[l]
                l += 1
            r += 1
        return ans if ans!=1e9 else 0

class PrefixSum:
    """
    * subarray_sum: 합이 정확히 k인 부분 배열의 개수 -- 누적합 + 해시맵 (음수 포함 가능)
    """
    def subarray_sum(arr, k):
        from collections import defaultdict
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = cur = 0
        for x in arr:
            cur += x
            ans += cnt[cur - k]
            cnt[cur] += 1
        return ans

arr = [3, -1, 2, 1]
k = 3
print(PrefixSum.subarray_sum(arr, k))
