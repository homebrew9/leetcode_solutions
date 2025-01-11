from typing import List

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        cnt = 0
        size = len(nums)
        for i in range(0, size-3):
            for j in range(i+1, size-2):
                for k in range(j+1, size-1):
                    for l in range(k+1, size):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            print(f'\t{nums[i]} + {nums[j]} + {nums[k]} == {nums[l]} ; ({i} + {j} + {k} == {l})')
                            cnt += 1
        return cnt
 
# Main section
for nums in [
               [1,2,3,6],
               [3,3,6,4,5],
               [1,1,1,3,5],
               [1,1,2,3,3,1,2,1,3,6,5,7],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.countQuadruplets(nums)
    print(f'r = {r}')
    print('================')

