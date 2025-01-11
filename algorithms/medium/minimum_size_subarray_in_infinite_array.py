#
# WC-365
# Does not work for last test case.
#
from typing import List

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        res = float('inf')
        arr = nums + nums
        N = len(arr)
        i, j = 0, 1
        currSum = arr[i] + arr[j]
        while True:
            #print(f'i, j, currSum = {i}, {j}, {currSum}')
            if currSum < target:
                j += 1
                if j >= N:
                    break
                currSum += arr[j]
            elif currSum > target:
                i += 1
                if i >= N:
                    break
                currSum -= arr[i-1]
            else:
                res = min(res, j-i+1)
                j += 1
                if j >= N:
                    break
                currSum += arr[j]
        return -1 if res == float('inf') else res
                

# Main section
for nums, target in [
                       ([1,2,3], 5),
                       ([1,1,1,2,3], 4),
                       ([2,4,6,8], 3),
                       ([1,2,2,2,1,2,1,2,1,2,1], 83),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.minSizeSubarray(nums, target)
    print(f'r = {r}')
    print('=================')

