from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #arr = [[] for _ in range(10**5 + 1)]
        arr = [[] for _ in range(len(nums)+1)]
        hsh = defaultdict(int)
        for n in nums:
            hsh[n] += 1
        for key, val in hsh.items():
            arr[val] += [key]
        print(f'\thsh = {hsh}')
        print(f'\tarr = {arr}')
        res = list()
        for i in range(len(arr)-1, -1, -1):
            if arr[i] is not None:
                res += [i for i in arr[i]]
                k -= len(arr[i])
                if k == 0:
                    return res
        #return res

# Main section
for nums, k in [
                  ([1,1,1,2,2,3], 2),
                  ([1], 1),
                  ([8,7,8,3,8,7,8,2,8,2,7,2,8,3,8,7,3,7,2,3,7,3,1,8,3,1,7,7,1,8], 4),
                  ([1,2], 2),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.topKFrequent(nums, k)
    print(f'r = {r}')
    print('==============')


