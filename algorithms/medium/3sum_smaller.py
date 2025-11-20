from typing import List
import bisect

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # We do a nested loop with O(N^2) time for nums[i] and nums[j], and
        # then a Binary Search for (target - nums[i] - nums[j]). Be careful
        # of the type of bisect (right/left) and how the diff is found!
        nums.sort()
        N = len(nums)
        res = 0
        for i in range(N):
            for j in range(i+1, N):
                delta = target - (nums[i] + nums[j]) - 1
                idx = bisect.bisect_right(nums, delta)
                res += max(idx - 1 - j, 0)
        return res

# Main section
for nums, target in [
                       ([-2,0,1,3], 2),
                       ([], 0),
                       ([0], 0),
                       ([5,2,4,0,5,1,-5,1,3,-1], 17),
                       ([-73,1,88,51,-63,61,100,76,-91,-20,-47,-19,25,-83,-15,-91,7,-60,-73,-70,-74,96,89,89,84,-74,29,-25,-9,-57], 91),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.threeSumSmaller(nums, target)
    print(f'r = {r}')
    print('=====================')











