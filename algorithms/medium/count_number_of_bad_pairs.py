from typing import List
from collections import defaultdict
import math

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # Intuition: j - i != nums[j] - nums[i] => nums[i] - i != nums[j] - j
        # We can find the pairs where nums[i] - i == nums[j] - j and subtract that from the total.
        # If we have n elements in a list, then the number of distinct pairs that we can be formed
        # from those n elements is nC2 = n! / (n-2)! / 2! or math.comb(n, 2)
        hsh = defaultdict(list)
        for i, v in enumerate(nums):
            hsh[v - i] += [i]
        good_pairs = 0
        for v in hsh.values():
            good_pairs += math.comb(len(v), 2)
        total_pairs = math.comb(len(nums), 2)
        bad_pairs = total_pairs - good_pairs
        return bad_pairs

# Main section
for nums in [
               [4,1,3,3],
               [1,2,3,4,5] ,
               [14,15,15,18,16,15,17,7,17,5,20,17,6,7,15,2,17,3,9,8,4,7,10,7,5,13,4,2,3,12],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.countBadPairs(nums)
    print(f'r = {r}')
    print('=========================')

