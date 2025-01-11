from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) < x:
            return -1
        N = len(nums)
        INF = 10 ** 20
        res = INF
        suffix_seen = dict()
        suffix_seen[0] = 0
        current = 0
        # Iterate from right to left and calculate the number of removals for various values of x
        for i, v in enumerate(reversed(nums)):
            current += v
            suffix_seen[current] = i + 1
        if x in suffix_seen:
            res = min(res, suffix_seen[x])
        #print(suffix_seen)
        # Now iterate from left to right and compare with the keys in suffix_seen
        current = 0
        for i, v in enumerate(nums):
            # current + suffix_seen = x => suffix_seen = x - current
            current += v
            if x - current in suffix_seen:
                res = min(res, suffix_seen[x - current] + (i + 1))
        if res == INF:
            return -1
        return res

# Main section
for nums, x in [
                  ([1,1,4,2,3], 5),
                  ([5,6,7,8,9], 4),
                  ([3,2,20,1,1,3], 10),
                  ([1,2,100,101,102], 3),
                  ([100,101,102,1,1], 2),
                  ([1,100,101,102,2], 3),
                  ([1,1,100,101,102,2], 2),
                  ([2,10,11,1], 2),
                  ([1,100,101,2], 3),
               ]:
    print(f'nums, x = {nums}, {x}')
    sol = Solution()
    r = sol.minOperations(nums, x)
    print(f'r = {r}')
    print('====================')


