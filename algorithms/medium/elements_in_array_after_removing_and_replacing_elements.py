from typing import List

class Solution:
    #def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    #    N = len(nums)
    #    res = list()
    #    for t, i in queries:
    #        p, q = divmod(t, N)
    #        if q == 0:
    #            if p % 2 == 1:
    #                arr = []
    #            else:
    #                arr = nums
    #        else:
    #            if p % 2 == 1:
    #                arr = nums[:q]
    #            else:
    #                arr = nums[q:]
    #        if i < len(arr):
    #            res.append(arr[i])
    #        else:
    #            res.append(-1)
    #    return res

    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        res = list()
        for t, i in queries:
            p, q = divmod(t, N)
            if p % 2 == 1:
                arr = nums[:q]
            else:
                arr = nums[q:]
            if i < len(arr):
                res.append(arr[i])
            else:
                res.append(-1)
        return res

# Main section
for nums, queries in [
                        ([0,1,2], [[0,2],[2,0],[3,2],[5,0]]),
                        ([2], [[0,0],[1,0],[2,0],[3,0]]),
                     ]:
    print(f'nums, queries = {nums}, {queries}')
    sol = Solution()
    r = sol.elementInNums(nums, queries)
    print(f'r = {r}')
    print('=====================')


