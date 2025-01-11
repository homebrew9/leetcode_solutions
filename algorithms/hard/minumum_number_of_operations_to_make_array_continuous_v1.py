from typing import List
from bisect import bisect_right

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))
        #print(f'\tn, new_nums = {n}, {new_nums}')
        #print('=====')
        for i in range(len(new_nums)):
            #print(f'\ti, new_nums[i] = {i}, {new_nums[i]}')
            left = new_nums[i]
            right = left + n - 1
            j = bisect_right(new_nums, right)
            #print(f'\tleft, right, j, new_nums[j] = {left}, {right}, {j}, {new_nums[j]}')
            #print(f'\tleft, right, j = {left}, {right}, {j}')
            count = j - i
            ans = min(ans, n - count)
            #print(f'\tcount, (n-count), ans = {count}, {n-count}, {ans}')
            #print('=====')
        return ans

# Main section
for nums in [
               [57,11,29,13,14],
               [4,2,5,3],
               [1,2,3,5,6],
               [1,10,100,1000],
               [1,51,52,53,100],
               [1,51,52,52,53,100],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minOperations(nums)
    print(f'r = {r}')
    print('======================')


