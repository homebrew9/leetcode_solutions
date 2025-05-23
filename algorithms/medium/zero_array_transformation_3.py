from typing import List
from heapq import heappush, heappop

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        heap = []
        deltaArray = [0] * (len(nums) + 1)
        operations = 0
        j = 0
        for i, num in enumerate(nums):
            operations += deltaArray[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
            while operations < num and heap and -heap[0] >= i:
                operations += 1
                deltaArray[-heappop(heap) + 1] -= 1
            if operations < num:
                return -1
        return len(heap)
 
# Main section
for nums, queries in [
                        ([2,0,2], [[0,2],[0,2],[1,1]]),
                        ([1,1,1,1], [[1,3],[0,2],[1,3],[1,2]]),
                        ([1,2,3,4], [[0,3]]),
                     ]:
    print(f'nums = {nums}')
    print(f'queries = {queries}')
    sol = Solution()
    r = sol.maxRemoval(nums, queries)
    print(f'r = {r}')
    print('============================')



















