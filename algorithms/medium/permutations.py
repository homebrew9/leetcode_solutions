from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def slideThrough(k, arr):
            #print(f'\t\tk, arr = {arr}, {k}')
            res = list()
            for item in arr:
                for i in range(len(item)+1):
                    res.append(item[:i] + [k] + item[i:])
            return res

        def permutation(arr):
            if len(arr) == 0:
                return [arr]
            #print(f'\tarr, arr[:-1], arr[-1] = {arr}, {arr[:-1]}, {arr[-1]}')
            #return permutation(slideThrough(arr[:-1], arr[-1]))
            return slideThrough(arr[0], permutation(arr[1:]))

        return permutation(nums)

# Main section
for nums in [
               [1],
               [1,2],
               [1,2,3],
               [1,2,3,4],
               [1,2,3,4,5],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.permute(nums)
    print(f'r = {r}')
    print('==================')




def slideThrough(arr, k):
    print(f'\t\tarr, k = {arr}, {k}')
    res = list()
    for i in range(len(arr)+1):
        res.append(arr[:i] + [k] + arr[i:])
    return res

