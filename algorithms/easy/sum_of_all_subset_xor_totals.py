from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Algorithm A: In this algorithm, we generate all subsets first. Then we do XOR
        # of each subset, adding them up.
        def all_subsets(i, arr):
            if i >= N:
                subsets.append(arr)
                return
            all_subsets(i + 1, arr)             # do not include nums[i]
            all_subsets(i + 1, arr + [nums[i]]) # include nums[i]
        N = len(nums)
        subsets = list()
        all_subsets(0, [])
        # Now add up all the XOR totals
        res = 0
        for subset in subsets:
            total = 0
            for element in subset:
                total ^= element
            res += total
        return res

    def subsetXORSum_1(self, nums: List[int]) -> int:
        # Algorithm B: We generate XOR totals of all subsets recursively. Very similar to Algorithm A,
        # except that we recursively calculate XOR sum instead of generating all subsets.
        def all_subsets(i, total):
            if i >= N:
                self.res += total
                return
            all_subsets(i + 1, total)             # do not include nums[i]
            all_subsets(i + 1, total ^ nums[i])   # include nums[i]
        N = len(nums)
        self.res = 0
        all_subsets(0, 0)
        return self.res

    def subsetXORSum_2(self, nums: List[int]) -> int:
        # Algorithm C: We generate sum of XOR totals of all subsets recursively.
        # This is cleaner than Algorithm B; it does not require a class variable.
        def dfs(i, total):
            if i >= N:
                return total
            # do not include nums[i] + include nums[i] in XOR total
            return dfs(i + 1, total) + dfs(i + 1, total ^ nums[i])
        N = len(nums)
        return dfs(0, 0)

# Main section
for nums in [
               [1,3],
               [5,1,6],
               [3,4,5,6,7,8],
               [19,13,16,10,6,20,14,2,5,19,11,16],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.subsetXORSum(nums)
    r1 = sol.subsetXORSum_1(nums)
    r2 = sol.subsetXORSum_2(nums)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print('========================')

