from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        N = len(nums)
        rem = sum(nums) % p
        if rem == 0:
            return 0
        pfx = [0 for _ in range(N)]
        for i in range(N):
            pfx[i] = nums[i] if i == 0 else pfx[i-1] + nums[i]
        arr = [x % p for x in pfx]
        hsh = {0: -1}
        res = N
        for i, v in enumerate(arr):
            n = (v - rem + p) % p
            if n in hsh:
                res = min(res, i - hsh[n])
            hsh[v] = i
        return -1 if res == N else res

# Main section
for nums, p in [
                  ([3,1,4,2], 6),
                  ([6,3,5,2], 9),
                  ([1,2,3], 3),
               ]:
    print(f'nums, p = {nums}, {p}')
    sol = Solution()
    r = sol.minSubarray(nums, p)
    print(f'r = {r}')
    print('===========================')










