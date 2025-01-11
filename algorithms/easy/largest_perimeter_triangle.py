from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def isTriangle(a, b, c):
            if a+b > c and b+c > a and c+a > b:
                return True
            return False

        nums.sort()
        max_perimeter = 0
        iter = len(nums) - 3
        while iter >= 0:
            a = nums[iter]
            b = nums[iter+1]
            c = nums[iter+2]
            if isTriangle(a,b,c):
                max_perimeter = a + b + c
                return max_perimeter
            iter -= 1
        return max_perimeter

# Main section
for nums in [
               [2,1,2],
               [1,2,1],
               [1,5,9,6,7,9,18],
               [2,9,6,4,5,3,1,1,1],
               [2,9,4,4,5,3,1,1,1],
               [2,2,1,1,1],
               [2,1,1,1],
               [1,1,1,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.largestPerimeter(nums)
    print(f'r = {r}')
    print('=============================')

