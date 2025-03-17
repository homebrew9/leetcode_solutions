from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # TC = O(N), SC = O(N)
        unmatched = set()
        for n in nums:
            if n in unmatched:
                unmatched.remove(n)
            else:
                unmatched.add(n)
        # There should be no unmatched integer in the end
        return len(unmatched) == 0

# Main section
for nums in [
               [3,2,3,2,2,2],
               [1,2,3,4],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.divideArray(nums)
    print(f'r = {r}')
    print('================')

