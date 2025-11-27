from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            if n % 3 != 0:
                res += 1
        return res

    def minimumOperations_1(self, nums: List[int]) -> int:
        return sum(n % 3 != 0 for n in nums)

    def minimumOperations_2(self, nums: List[int]) -> int:
        return sum(map(lambda x: bool(x % 3), nums))

# Main section
for nums in [
               [1,2,3,4],
               [3,6,9],
               [24,48,28,49,16,33,15,4,25,14,7,47,25,5,25,13,26,38,6,21,32,43,26,22,1,3,49,37,30,43,4,46,40,1,26,18,24,12,47,8,37,38,36,41,22,18,42,20,28,31],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minimumOperations(nums)
    r1 = sol.minimumOperations_1(nums)
    r2 = sol.minimumOperations_2(nums)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    assert(r == r1 == r2)
    print('===========================')




