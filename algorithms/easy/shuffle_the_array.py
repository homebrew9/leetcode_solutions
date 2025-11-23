from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = list()
        for i in range(n):
            res.extend([nums[i], nums[i+n]])
        return res

    def shuffle_1(self, nums: List[int], n: int) -> List[int]:
        arr = []
        for a, b in zip(nums[:n], nums[n:]):
            arr += [a, b]
        return arr

# Main section
for nums, n in [
                  ([2,5,1,3,4,7], 3),
                  ([1,2,3,4,4,3,2,1], 4),
                  ([1,1,2,2], 2),
               ]:
    print(f'nums, n = {nums}, {n}')
    sol = Solution()
    r = sol.shuffle(nums, n)
    r1 = sol.shuffle_1(nums, n)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('===========================')








