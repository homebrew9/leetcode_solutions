from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        N = len(nums)
        rpfx = [0] * N
        for i in range(N-1, -1, -1):
            rpfx[i] = nums[i] if i == N-1 else nums[i] + rpfx[i+1]
        res = 0
        for i in range(N-1):
            if nums[i] > rpfx[i+1] / (N - i - 1):
                res += 1
        return res

    def dominantIndices_1(self, nums: List[int]) -> int:
        N = len(nums)
        arr = [0.0] * N
        total = 0
        for i in range(N-1, -1, -1):
            total += nums[i]
            arr[i] = total / (N - i)
        return sum(nums[i] > arr[i+1] for i in range(N-1))

    def dominantIndices_2(self, nums: List[int]) -> int:
        def solve(i):
            nonlocal res
            if i == N-1:
                return nums[i]
            val = solve(i+1)
            if nums[i] > val / (N - i - 1):
                res += 1
            return val + nums[i]
        N = len(nums)
        res = 0
        solve(0)
        return res

# Main section
for nums in [
               [5,4,3],
               [4,1,2],
               [10,9,8,7,6,5,4,3,2,1],
               [1,2,1,2,1,2,1,2,1,2,1],
               [16,44,86,98,24,64,7,62,81,44,6,26,26,96,65,51,28,75,81,25,74,37,51,36,74,64,47,61,52,16,75,22,78,6,44,93,88,24,50,59],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.dominantIndices(nums)
    r1 = sol.dominantIndices_1(nums)
    r2 = sol.dominantIndices_2(nums)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    assert(r == r1 == r2)
    print('=================================================')
 
















