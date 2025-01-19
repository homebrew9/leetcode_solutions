#
# Shorter Binary Search
#
from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        def get_total(n):
            nums = set(range(1, n+1)) - banned_set
            return sum(nums), len(nums)
        banned_set = set(banned)
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            total, res = get_total(mid)
            #print(left, right, mid, total, res)
            if total <= maxSum:
                left = mid + 1
            else:
                right = mid - 1
        _, res = get_total(right)
        return res

# Main section
for banned, n, maxSum in [
                            ([1,6,5], 5, 6),
                            ([1,2,3,4,5,6,7], 8, 1),
                            ([11], 7, 50),
                            ([176,36,104,125,188,152,101,47,51,65,39,174,29,55,13,138,79,81,175,178,42,108,24,80,183,190,123,20,139,22,140,62,58,137,68,148,172,76,173,189,151,186,153,57,142,105,133,114,165,118,56,59,124,82,49,94,8,146,109,14,85,44,60,181,95,23,150,97,28,182,157,46,160,155,12,67,135,117,2,25,74,91,71,98,127,120,130,107,168,18,69,110,61,147,145,38], 3016, 240),
                         ]:
    print(f'banned, n, maxSum = {banned}, {n}, {maxSum}')
    sol = Solution()
    r = sol.maxCount(banned, n, maxSum)
    print(f'r = {r}')
    print('================')

