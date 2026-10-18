from typing import List
from collections import defaultdict

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            res = 0
            while n > 0:
                q, r = divmod(n, 10)
                res += r
                n = q
            return res
        # Compare the original list with the sorted list. Go through each index
        # and cycle through its positions until it forms a loop. If the required
        # arrangement could be decomposed into disjoint cycles, then the minimum
        # swaps needed equals: total_swaps = N - (number_of_cycles). Here, we
        # include stationary indexes as cycles of length 1. Selection sort does
        # replicate it, but being O(N^2), it will time out for 10^5 elements.
        # nums = [3, 1, 2, 4, 5, 7, 8, 6, 9, 10] ; N = 10
        # cycles = (3 -> 1 -> 2), 4, 5, (7 -> 8 -> 6), 9, 10 = 6 (Lengths = 3,1,1,3,1,1)
        # Min swaps = 10 - 6 = 4
        N = len(nums)
        arr = sorted(range(N), key=lambda i: (digit_sum(nums[i]), nums[i]))
        hsh = defaultdict(int)
        for i, v in enumerate(arr):
            hsh[v] = i
        visited = set()
        res = 0
        for i in range(N):
            # Construct a cycle from this index and add len(cycle)-1 to
            # to the total number of swaps. This is slightly different from
            # the logic above, but this avoids going through cycles of length 1.
            if i in visited:
                continue
            length = 0
            node = i
            while True:
                visited.add(node)
                node = hsh[node]
                length += 1
                if node == i:
                    break
            res += length - 1
        return res

# Main section
for nums in [
               [37,100],
               [22,14,33,7],
               [18,43,34,16],
               [169, 144, 426, 598, 246, 67, 789, 704, 450, 21],
               [1,2,3,4,5,6,7,8,9],
               [10,5,7,12,23,37,19,13,51,83],
               [688129, 294919, 163850, 163851, 360459, 15, 786451, 393236, 688150, 688153, 622618, 688159, 917542, 229418, 917550, 589871, 491569, 917556, 983093],
               [336855040, 920911872, 626786309, 798490636, 614203405, 664797199, 920125457, 30933009, 109314065, 209190930, 313786390, 211550231, 301989911],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minSwaps(nums)
    print(f'r = {r}')
    print('===================================')


