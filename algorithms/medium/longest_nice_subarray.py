from typing import List
import numpy as np

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        def update_bits(n, operation):
            lst = [int(x) for x in bin(n).replace('0b','').zfill(30)]
            if operation == 'add':
                self.arr = list(np.array(self.arr) + np.array(lst))
            elif operation == 'subtract':
                self.arr = list(np.array(self.arr) - np.array(lst))
        self.arr = [0 for _ in range(30)]
        N = len(nums)
        i = 0
        res = 0
        for j in range(N):
            update_bits(nums[j], 'add')
            while any([x > 1 for x in self.arr]):
                update_bits(nums[i], 'subtract')
                i += 1
            res = max(res, j - i + 1)
        return res

    def longestNiceSubarray_1(self, nums: List[int]) -> int:
        def add_bits(n):
            lst = [int(x) for x in bin(n).replace('0b','').zfill(30)]
            for i in range(30):
                arr[i] += lst[i]
        def subtract_bits(n):
            lst = [int(x) for x in bin(n).replace('0b','').zfill(30)]
            for i in range(30):
                arr[i] -= lst[i]
        N = len(nums)
        arr = [0 for _ in range(30)]
        i = 0
        res = 0
        for j in range(N):
            add_bits(nums[j])
            while any([x > 1 for x in arr]):
                subtract_bits(nums[i])
                i += 1
            res = max(res, j - i + 1)
        return res

# Main section
for nums in [
               [1,3,8,48,10],
               [3,1,5,11,13],
               [1,2,3,4,5,6,7,8,9,10],
               [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.longestNiceSubarray(nums)
    r1 = sol.longestNiceSubarray_1(nums)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('================')

