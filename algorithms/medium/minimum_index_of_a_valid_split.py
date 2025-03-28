from typing import List
from collections import defaultdict

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N = len(nums)
        hsh = defaultdict(int)
        for n in nums:
            hsh[n] += 1
        dom_elem, right_freq = sorted(hsh.items(), key=lambda x: (-x[1], x[0]))[0]
        left_freq = 0
        for i in range(0, N-1):
            if nums[i] == dom_elem:
                left_freq += 1
                right_freq -= 1
                if left_freq * 2 > i + 1 and right_freq * 2 > N - i - 1:
                    return i
        return -1

# Main section
for nums in [
               [1,2,2,2],
               [2,1,3,1,1,1,7,1,2,1],
               [3,3,3,3,7,2,2],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minimumIndex(nums)
    print(f'r = {r}')
    print('========================')

