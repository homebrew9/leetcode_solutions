from typing import List

class Solution:
    def onceTwice(self, nums: List[int]) -> List[int]:
        once, twice = set(), set()
        for n in nums:
            if n in twice:
                twice.remove(n)
            elif n in once:
                once.remove(n)
                twice.add(n)
            else:
                once.add(n)
        return [list(once)[0], list(twice)[0]]

# Main section
for nums in [
               [2,2,3,2,5,5,5,7,7],
               [4,4,6,4,9,9,9,6,8],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.onceTwice(nums)
    print(f'r = {r}')
    print('===========================')


