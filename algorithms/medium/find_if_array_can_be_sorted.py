from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def bit_count(n):
            res = 0
            while n > 0:
                res += (n & 1)
                n >>= 1
            return res
        N = len(nums)
        arr = [bit_count(x) for x in nums]
        prev, min_elem, max_elem = None, None, None
        lst = list()
        for i in range(N):
            if prev is None or arr[i] != prev:
                if min_elem and max_elem:
                    lst.append([min_elem, max_elem])
                min_elem, max_elem = nums[i], nums[i]
            else:
                min_elem = min(min_elem, nums[i])
                max_elem = max(max_elem, nums[i])
            prev = arr[i]
        if min_elem and max_elem:
            lst.append([min_elem, max_elem])
        for i in range(1, len(lst)):
            if lst[i][0] < lst[i-1][1]:
                return False
        return True

# Main section
for nums in [
               [8,4,2,30,15],
               [1,2,3,4,5],
               [3,16,8,4,2],
               [16,245,125],
               [2,17],
               [109,160,68,18,21,158,37,68,132,28,114,155,99,212,18,187,53,89,85,246,250,44,68,247,41,174,232,218,213,241,3,190,109,140,95,86,15,114,29,195,204,194,94,213,113,70,99,233,216,236,251,47,116,213,215,6,148,159,153,209,189,217,230,242,119,227,217,45,11,106,111,232,225,207,99,223,231,160,97,127,154,127,171,59,113,178,60,159,39,2,152,49,236,227,250,153,243,55,8,168],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.canSortArray(nums)
    print(f'r = {r}')
    print('================')


