from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum([int(x) for x in str(n)])
        def determine_min_swaps(arr1, arr2):
            N = len(arr1)
            pos = dict()
            for i in range(N):
                pos[arr1[i]] = i
            swaps = 0
            for i in range(N):
                if arr2[i] != arr1[i]:
                    ind = pos[arr2[i]]
                    arr1[i], arr1[ind] = arr1[ind], arr1[i]
                    pos[arr1[i]] = i
                    pos[arr1[ind]] = ind
                    swaps += 1
            return swaps
        arr = [(x, digit_sum(x)) for x in nums]
        arr = sorted(arr, key=lambda x: (x[1], x[0]))
        lst_digit_sum_sorted = [x for x, ds in arr]
        res = determine_min_swaps(nums, lst_digit_sum_sorted)
        return res

# Main section
for nums in [
               [37,100],
               [22,14,33,7],
               [18,43,34,16],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minSwaps(nums)
    print(f'r    = {r}')
    print('============================')

