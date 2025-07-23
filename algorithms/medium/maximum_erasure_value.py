from collections import defaultdict
from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        seen = set()
        curr = 0
        res = float('-inf')
        left, right = 0, 0
        while right < N:
            if nums[right] in seen:
                while True:
                    curr -= nums[left]
                    seen.remove(nums[left])
                    left += 1
                    if nums[left - 1] == nums[right]:
                        break
            seen.add(nums[right])
            curr += nums[right]
            res = max(res, curr)
            right += 1
        return res
    def maximumUniqueSubarray_1(self, nums: List[int]) -> int:
        # This algorithm is highly inefficient for large arrays with all distinct elements.
        # For example, it throws TLE for the test case: list(range(1, 10001))
        # The reason is that the check: "set(hsh.values()) == {1}" gets very expensive as
        # the dictionary grows to 10K unique keys. The other method uses an efficient algorithm.
        # It uses a set that has O(1) lookup. Whenever there is a potential conflict, it keeps
        # removing elements from the left until we have removed the conflicting integer.
        N = len(nums)
        hsh = defaultdict(int)
        curr = 0
        res = float('-inf')
        left, right = 0, 0
        while right < N:
            curr += nums[right]
            hsh[nums[right]] += 1
            while not ( set(hsh.values()) == {1} ):
                curr -= nums[left]
                hsh[nums[left]] -= 1
                if hsh[nums[left]] == 0:
                    del hsh[nums[left]]
                left += 1
            res = max(res, curr)
            right += 1
        return res

# Main section
for nums in [
               [4,2,4,5,6],
               [5,2,1,2,5,2,1,2,5],
               [14,21,25,12,29,5,27,22,23,1,25,12,21,4,23,17,3,26,6,12,11,29,24,2,24,18,29,12,10,7,18,18,11,25,7,2,5,25,4,3],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maximumUniqueSubarray(nums)
    print(f'r  = {r}')
    r1 = sol.maximumUniqueSubarray_1(nums)
    print(f'r1 = {r1}')
    print('============================')



