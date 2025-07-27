from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        def remove_repetitions(nums):
            lst = list()
            N = len(nums)
            i, j = 0, 1
            lst.append(nums[i])
            while j < N:
                if nums[j] != nums[i]:
                    lst.append(nums[j])
                    i = j
                j += 1
            return lst
        arr = remove_repetitions(nums)
        res = 0
        N = len(arr)
        for i in range(1, N-1):
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:   # Hill
                res += 1
            elif arr[i-1] > arr[i] and arr[i] < arr[i+1]: # Valley
                res += 1
        return res

# Main section
for nums in [
               [2,4,1,1,6,5],
               [6,6,5,5,4,1],
               [2,1,1,1,5,2,2,1,2],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.countHillValley(nums)
    print(f'r = {r}')
    print('==========================')












