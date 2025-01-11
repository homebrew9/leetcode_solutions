#
# Both the recursive methods below throw TLE for the last 2 test cases!!
#
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def check(arr):
            #print(f'\tarr = {arr}')
            if sum(arr) == target:
                self.res += [arr]
                return
            if sum(arr) > target:
                return
            for n in nums:
                if sum(arr + [n]) <= target:
                    check(arr + [n])
        self.res = list()
        for n in nums:
            if n <= target:
                check([n])
        #print(self.res)
        return len(self.res)
    #def combinationSum4(self, nums: List[int], target: int) -> int:
    #    def check(delta):
    #        if delta == 0:
    #            return 1
    #        cnt = 0
    #        for n in nums:
    #            if n <= delta:
    #                cnt += check(delta - n)
    #        return cnt
    #    return check(target)

# Main section
for nums, target in [
                       ([1,2,3], 4),
                       ([9], 3),
                       ([4,2,1], 32),
                       ([1,2,3,4,5], 120),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.combinationSum4(nums, target)
    print(f'r = {r}')
    print('=================')

