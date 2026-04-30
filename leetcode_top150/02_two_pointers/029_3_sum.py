"""LeetCode Top 150
Level:
    Medium
Status:
    Failed
Note:
    

Thu Apr 30 23:11:15 KST 2026
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()

        ans = []
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            ni = nums[i]
            if ni>0:
                break
            
            j, k = i+1, n-1
            while j < k:
                nj, nk = nums[j], nums[k]
                if ni+nj+nk == 0:
                    # if [ni, nj, nk] in ans: has additional O(N)
                    ans.append([ni, nj, nk])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif ni+nj+nk < 0:
                    j += 1
                else:
                    k -= 1

        return ans
