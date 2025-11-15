from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Just follow the hints
        N = len(nums)
        if N <= 2:
            return N
        pref = [1] * N
        for i in range(1, N):
            if nums[i] >= nums[i-1]:
                pref[i] = pref[i-1] + 1
        suff = [1] * N
        for i in range(N-2, -1, -1):
            if nums[i] <= nums[i+1]:
                suff[i] = suff[i+1] + 1
        #print(f'pref = {pref}')
        #print(f'suff = {suff}')
        res = max(max(pref), max(suff))
        span = 0
        for i in range(N):
            if i == 0:
                span = suff[i+1] + 1
            elif i == N - 1:
                span = pref[i-1] + 1
            else:
                # Check if we can combine left and right subarays.
                # Otherwise, we can always pick the larger of the two and add 1.
                if nums[i+1] >= nums[i-1]:
                    span = pref[i-1] + suff[i+1] + 1
                else:
                    span = max(pref[i-1], suff[i+1]) + 1
            res = max(res, span)
        return res

# Main section
for nums in [
               [1,2,3,1,2],
               [2,2,2,2,2],
               [4],
               [-5,1,-1,-8,-5],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.longestSubarray(nums)
    print(f'r = {r}')
    print('=====================')





































