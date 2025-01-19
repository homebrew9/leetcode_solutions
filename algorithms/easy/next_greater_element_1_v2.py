from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Key intuition: We can build a dictionary of all elements in nums2 and
        # their next higher element using a stack!!!
        hsh = dict()
        stack = list()
        for n in nums2:
            while stack and stack[-1] < n:
                hsh[stack.pop()] = n
            stack.append(n)
        while stack:
            hsh[stack.pop()] = -1
        return [hsh[n] for n in nums1]

# Main section
for nums1, nums2 in [
                       ([0,15,9,22,1], [2,9,1,4,15,3,22,0]),
                       ([4,1,2], [1,3,4,2]),
                       ([2,4], [1,2,3,4]),
                       ([2], [2]),
                       ([2], [2,3]),
                       ([2], [2,0]),
                       ([1,2,3,4,5,6], [6,5,4,3,2,1]),
                       ([1,2,3,4,5,6], [9,8,7,6,5,4,3,2,1]),
                       ([1,2,3,4,5,6], [1,2,3,4,5,6,7,8,9]),
                       ([1,2,3,4,5,6], [1,2,3,4,5,6]),
                    ]:
    print(f'nums1 = {nums1} ; nums2 = {nums2}')
    sol = Solution()
    r = sol.nextGreaterElement(nums1, nums2)
    print(f'r = {r}')
    print('======================')


