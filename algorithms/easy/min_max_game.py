from typing import List

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            print(n)
            # Process n elements, update the first n//2 elements
            oper = 'min'
            pos = 0
            for i in range(0,n,2):
                print(f'\ti = {i}')
                if oper == 'min':
                    nums[pos] = min(nums[i], nums[i+1])
                    oper = 'max'
                elif oper == 'max':
                    nums[pos] = max(nums[i], nums[i+1])
                    oper = 'min'
                pos += 1
                print(f'\t\t{nums}')
            print(f'{nums}')
            print('~~~~~~~')
            n //= 2
        return nums[0]

# Main section
for nums in [
               [1,3,5,2,4,8,2,2],
               [3],
               [5,7,3,1,9,11,7,8,13,23,77,66,230,378,91,73],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minMaxGame(nums)
    print(f'r = {r}')
    print('=======================')

