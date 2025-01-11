#
# Brilliant logic using stack!!!
# https://leetcode.com/problems/next-greater-element-i/discuss/824654/Python-3-greater-94.64-faster.-Used-stack-and-dictionary.-Explanation-added
# Make sure to trace the working of this and understand it as well.
#
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hsh = dict()
        stack = list()
        stack.append(nums2[0])
        for i in range(1, len(nums2)):
            #print(f'\t>>>i, nums2[i], stack, hsh = {i}, {nums2[i]}, {stack}, {hsh}')
            while stack and nums2[i] > stack[-1]:
                hsh[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
            print(f'\t>>>i, nums2[i], stack, hsh = {i}, {nums2[i]}, {stack}, {hsh}')
        print(hsh)
        print(stack)
        return []

# Main section
sol = Solution()
for nums1, nums2 in [
                       ([0,15,9,22,1], [2,9,1,4,15,3,22,0]),
                       #([4,1,2], [1,3,4,2]),
                       #([2,4], [1,2,3,4]),
                       #([2], [2]),
                       #([2], [2,3]),
                       #([2], [2,0]),
                       #([1,2,3,4,5,6], [6,5,4,3,2,1]),
                       #([1,2,3,4,5,6], [9,8,7,6,5,4,3,2,1]),
                       #([1,2,3,4,5,6], [1,2,3,4,5,6,7,8,9]),
                       #([1,2,3,4,5,6], [1,2,3,4,5,6]),
                    ]:
    print(f'nums1 = {nums1} ; nums2 = {nums2}')
    r = sol.nextGreaterElement(nums1, nums2)
    print(f'r = {r}')
    print('======================')


