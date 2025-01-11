from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        def listProduct(arr):
            # len(arr) is > 0
            prd = 1
            for x in arr:
                prd *= x
            return prd
        nums.sort()
        pos, neg, zeros = 0, 0, 0
        for n in nums:
            if n < 0:
                neg += 1
            elif n > 0:
                pos += 1
            else:
                zeros += 1
        # 1) Only one of neg, zeros, pos is > 0; the rest are zeros
        if neg > 0 and zeros == 0 and pos == 0:
            if neg == 1:
                return nums[0]
            if neg % 2 == 0:
                arr = nums[:neg]
            else:
                arr = nums[:neg-1]
            return listProduct(arr)
        if neg == 0 and zeros > 0 and pos == 0:
            return 0
        if neg == 0 and zeros == 0 and pos > 0:
            return listProduct(nums)
        # 2) Any two of (neg, zeros, pos) is > 0 the third is 0
        if neg == 0 and zeros > 0 and pos > 0:
            return listProduct(nums[-pos:])
        if neg > 0 and zeros > 0 and pos == 0:
            if neg == 1:
                prd1 = nums[0]
            elif neg % 2 == 0:
                arr = nums[:neg]
                prd1 = listProduct(arr)
            else:
                arr = nums[:neg-1]
                prd1 = listProduct(arr)
            return max(prd1, 0)
        if neg > 0 and zeros == 0 and pos > 0:
            if neg == 1:
                prd1 = 1
            elif neg % 2 == 0:
                arr = nums[:neg]
                prd1 = listProduct(arr)
            else:
                arr = nums[:neg-1]
                prd1 = listProduct(arr)
            prd2 = listProduct(nums[-pos:])
            return prd1 * prd2
        # 3) All of (neg, zeros, pos) are > 0
        if neg > 0 and zeros > 0 and pos > 0:
            if neg == 1:
                prd1 = 1
            elif neg % 2 == 0:
                arr = nums[:neg]
                prd1 = listProduct(arr)
            else:
                arr = nums[:neg-1]
                prd1 = listProduct(arr)
            prd2 = listProduct(nums[-pos:])
            return prd1 * prd2

# Main section
for nums in [
               [3,-1,-5,2,5,-9],
               [-4,-5,-4],
               [-1,-2,-3,-4,-5,0,0,0],
               [-1,-2,-3,-4,0,0,0],
               [-3],
               [-3,0,0],
               [0,0,3,4,5],
               [-3,0,0,3,4,5],
               [-3,-5,0,0,3,4,5],
               [-3,-5,-7,0,0,3,4,5],
               [-3,-5,-7,-9,0,0,3,4,5],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maxStrength(nums)
    print(f'r = {r}')
    print('==================')

