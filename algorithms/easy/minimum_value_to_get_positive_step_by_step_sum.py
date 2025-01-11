from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start = 1
        delta = 1
        for n in nums:
            if start + n < 1:
                curr = 1 - n - start
                start += curr
                delta += curr
            start += n
        return delta

# Main section
for nums in [
               [-3,2,-3,4,2],
               [1,2],
               [1,-2,-3],
               [73,88,-91,15,-35,96,2,52,-49,30,10,-42,48,-93,-47,-63,68,-78,-91,-75,-80,23,-55,-63,24,-80,78,61,-3,-94,43,-36,-79,-74,-88,43,-55,22,24,4,45,89,32,32,-91,18,51,-16,92,46,58,49,-92,-67,53,-99,-31,-91,-84,-93,66,56,85,73,-52,-32,30,-93,-10,85,-28,67,-46,-37,-44,-37,-63,-42,-53,-38,-73,36,-49,47,26,-7,55,-25,71,19,10,51,72,-21,98,36,-29,96,-76,-30],
               [2,3,4,5,6],
               [2,-3,-5,7,-4,-8],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minStartValue(nums)
    print(f'r = {r}')
    print('==============')

