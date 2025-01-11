from typing import List
import itertools

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        hsh = dict()
        for i in digits:
            hsh[i] = hsh.get(i,0) + 1
        noEvenExists = True
        for k in hsh.keys():
            if k % 2 == 0:
                noEvenExists = False
                break
        if noEvenExists:
            return []

        hsh1 = dict()
        for i, n in enumerate(digits):
            num = n
            arr = digits[:i] + digits[i+1:]
            #print(f'num = {num}')
            #print(f'arr = {arr}')
            if num in (0,2,4,6,8):
                for item in list(itertools.permutations(arr, 2)):
                    candidate = ''.join([str(j) for j in item]) + str(num)
                    if int(candidate) >= 100:
                        #print(f'\t>>> candidate = {candidate}')
                        hsh1[candidate] = 1
        res = list(hsh1.keys())
        res.sort()
        return res

# Main section
sol = Solution()
for digits in [
                 #[3,7,5],
                 #[2,2,8,8,2],
                 #[2,1,3,0],
                 #[0,2,0,0],
                 #[0,0,0],
                 #[0,1,2,3,4,5,6,7,8,9],
                 #[0,2,4,6,8],
                 #[1,8,7,7,1,1,5,4,0,0,7,5,1,7,9],
                 [7,2,9,8,0,9,8,9,1,2,0,2,4,0,5,0,2,4,8,9,4,8,1,0,3,7,6,4,1,8,9,2,4,5,1,5,1,3,5,5,8,9,2,6,0,7,1,3,7,5,3,0,6,7,7,6,3,7,4,5,5,1,5,6,9,9,3,3,1,2,3,1,6,4,0,8,4,8,1,7,0,8,4,3,7,9,9,6,5,3,7,8,6,6,6,4,2,0,2,2],
              ]:
    print(f'digits = {digits}')
    r = sol.findEvenNumbers(digits)
    print(f'r    = {r}')
    print('===========================')

