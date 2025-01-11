from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hsh = dict()
        max_count = 0
        cnt, first, last, distance = 1, None, None, None
        for i, n in enumerate(nums):
            if n in hsh:
                cnt = hsh[n][0] + 1
                first = hsh[n][1]
                last = i
                distance = last - first
                hsh[n] = [cnt, first, last, distance]
            else:
                hsh[n] = [1, i, i, 0]
            max_count = max(max_count, cnt)
        print(f'\thsh = {hsh} ; max_count = {max_count}')
        min_dist = float('inf')
        for k in hsh:
            val = hsh[k]
            if val[0] == max_count:
                if val[3] < min_dist:
                    min_dist = val[3]
        return min_dist + 1

# Main section
for nums in [
               [1,2,2,3,1],
               [1,2,2,3,1,4,2],
               [1,7,1,4,9,9,6,2,7,2,5,5,2,3,1,9,2,8,7,9,5,5,3,7],
               [1,4,5,2,7,8,3,9,5,9,3,5,7,2,2,2,1,7,9,7,5,9,1,6],
               [3,4,5,5,5,9,9,2,3,2,2,9,1,7,2,6,1,7,5,7,7,8,9,1],
               [1],
               [1,2],
               [1,1],
               [1,2,3],
               [1,2,3,1],
               [3,2,3,3,1,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findShortestSubArray(nums)
    print(f'r = {r}')
    print('==================')

