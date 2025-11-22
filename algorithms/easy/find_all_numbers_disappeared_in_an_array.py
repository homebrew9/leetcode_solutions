from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        seen = set(nums)
        res = list()
        for n in range(1, N + 1):
            if n not in seen:
                res.append(n)
        return res

    def findDisappearedNumbers_1(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1)) - set(nums))

    def findDisappearedNumbers_2(self, nums: List[int]) -> List[int]:
        # Iterate through nums. If an element is v then mark nums[v-1] as -nums[v-1].
        # This means that the number has been spotted. Don't mark a number more than once.
        # Use abs(v) while considering a number that is present.
        # TC = O(N), SC = O(1)
        #   0    1    2    3   4   5    6    7
        # [ 4 ,  3 ,  2 ,  7 , 8 , 2 ,  3 ,  1]
        # [-4 , -3 , -2 , -7 , 8 , 2 , -3 , -1]
        for n in nums:
            m = abs(n)
            if nums[m - 1] > 0:
                nums[m - 1] = -nums[m - 1]
        return [i + 1 for i, v in enumerate(nums) if v > 0]

# Main section
for nums in [
               [4,3,2,7,8,2,3,1],
               [1,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findDisappearedNumbers(nums)
    r1 = sol.findDisappearedNumbers_1(nums)
    r2 = sol.findDisappearedNumbers_2(nums)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print('===========================')

