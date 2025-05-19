from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        i = 0
        res = list()
        while i < N - 2:
            if nums[i] > 0:
                break
            ival = nums[i]
            j = i + 1
            k = N - 1
            while j < k:
                jval = nums[j]
                kval = nums[k]
                if jval + kval == -ival:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < N and nums[j] == jval:
                        j += 1
                    while k > i and nums[k] == kval:
                        k -= 1
                elif jval + kval < -ival:
                    j += 1
                else:
                    k -= 1
            while i < N-2 and nums[i] == ival:
                i += 1
        return res

# Main section
for nums in [
               [-1,0,1,2,-1,-4],
               [0,1,1],
               [0,0,0],
               [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.threeSum(nums)
    print(f'r    = {r}')
    print('============================')






