from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        def listProduct(arr):
            # len(arr) is > 0
            prd = 1
            for x in arr:
                prd *= x
            return prd
        pos, neg, zeros = list(), list(), 0
        for n in nums:
            if n < 0:
                neg.append(n)
            elif n > 0:
                pos.append(n)
            else:
                zeros += 1
        # Get the neg and pos products
        pos_prd = listProduct(pos) if len(pos) > 0 else 0
        if len(neg) > 1:
            if len(neg) % 2 == 0:
                neg_prd = listProduct(neg)
            else:
                neg_prd = listProduct(sorted(neg)[:-1])
        elif len(neg) == 1:
            neg_prd = neg[0]
        else:
            neg_prd = 0
        if pos_prd == 0:
            if zeros == 0:
                return neg_prd
            else:
                return max(neg_prd, 0)
        else:
            if neg_prd > 0:
                return neg_prd * pos_prd
            else:
                return pos_prd

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


