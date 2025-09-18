from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        # We try to solve the problem without using the "math" module.
        # Euclid gcd can also be found using iterative approach.
        def gcd_euclid(a, b):
            while b > 0:
                a, b = b, a % b
            return a
        stack = list()
        for n in nums:
            val = n
            while stack and (gcde := gcd_euclid(stack[-1], val)) > 1:
                m = stack.pop()
                val = (val * m) // gcde   # LCM(a, b) = (a * b) // GCD(a, b)
            stack.append(val)
        return stack

# Main section
for nums in [
               [6,4,3,2,7,6,2],
               [2,2,1,1,3,3,3],
               [287,41,49,287,899,23,23,20677,5,825],
               [2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,6,6],
               [29,29,29,481,481,6253,247,247,481,37,9139,9139,13,6253,13,6253,19,9139,169,481,3211,3211,169,169,9139,4693,6253,481,481,13,13,13,13,13,6253,13,13,169,169,169,247,247,9139,2197,247,3211,4693,247,247,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.replaceNonCoprimes(nums)
    print(f'r = {r}')
    print('===================')


































