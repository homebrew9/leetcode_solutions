from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        low, high = 0, len(nums) - 1
        found = False
        #print(f'\tlow, high = {low}, {high}')
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                found = True
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            #print(f'\tlow, mid, high = {low}, {mid}, {high}')
        #print(f'\tfound, low, mid, high = {found}, {low}, {mid}, {high}')
        res = []
        if found:
            i = mid
            while i >= 0:
                if nums[i] != target:
                    break
                i -= 1
            #print(f'\tleft-i = {i+1}')
            res += [i + 1]
            i = mid
            while i < len(nums):
                if nums[i] != target:
                    break
                i += 1
            #print(f'\tright-i = {i-1}')
            res += [i - 1]
        else:
            res += [-1, -1]
        #print('\t==============')
        return res

# Main section
for nums, target in [
                       ([5,7,7,8,8,10], 8),
                       ([5,7,7,8,8,10], 6),
                       ([], 0),
                       ([1], 0),
                       ([1], 1),
                       ([1], 2),
                       ([1,2,3,4,5,6,7,8,9,9,9,9,10], 9),
                       ([1,2,3,4,5,6,7,8,9,9,9,9,10], 5),
                       ([1,2,3,4,5,6,7,8,9,9,9,9,10], -9),
                       ([1,2,3,4,5,6,7,8,9,9,9,9,10], 99),
                       ([1,2,3,4,4,5,6,7,8,9,9,9,9,10], 4),
                       ([1,2,3,4,4,5,6,7,8,9,9,9,9,10], 1),
                       ([1,2,3,4,4,5,6,7,8,9,9,9,9,10], 10),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.searchRange(nums, target)
    print(f'r = {r}')
    print('=====================')

