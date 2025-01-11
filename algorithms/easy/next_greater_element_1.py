from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums2)
        hsh = dict()
        for i, v in enumerate(nums2):
            hsh[v] = i
        found = False

        arr = list()
        for n in nums1:
            #print(f'\tn = {n}')
            k = hsh[n]
            #print(f'\tk = {k}')
            for j in range(k+1, m):
                #print(f'\t\tj, nums2[j], n = {j}, {nums2[j]}, {n}')
                if nums2[j] > n:
                    #print(f'\t\t\tAppending nums2[j] = {nums2[j]}')
                    arr.append(nums2[j])
                    found = True
                    break
            if not found:
                #print(f'\tAppending -1')
                arr.append(-1)
            found = False
            #print('-----')
        return arr

# Main section
sol = Solution()
for nums1, nums2 in [
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
    r = sol.nextGreaterElement(nums1, nums2)
    print(f'r = {r}')
    print('======================')

