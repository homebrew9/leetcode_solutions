from typing import List
from collections import defaultdict

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        hsh = defaultdict(int)
        for d in digits:
            hsh[d] += 1
        res = list()
        for n in range(100, 1000, 2):
            hsh1 = defaultdict(int)
            z = n % 10
            y = n//10 % 10
            x = n//100
            hsh1[x] += 1
            hsh1[y] += 1
            hsh1[z] += 1
            for k, v in hsh1.items():
                if k not in hsh or hsh[k] < v:
                    break
            else:
                res.append(n)
        return res

# Main section
for digits in [
                 [2,1,3,0],
                 [2,2,8,8,2],
                 [3,7,5],
                 [1,8,7,7,1,1,5,4,0,0,7,5,1,7,9],
                 [7,2,9,8,0,9,8,9,1,2,0,2,4,0,5,0,2,4,8,9,4,8,1,0,3,7,6,4,1,8,9,2,4,5,1,5,1,3,5,5,8,9,2,6,0,7,1,3,7,5,3,0,6,7,7,6,3,7,4,5,5,1,5,6,9,9,3,3,1,2,3,1,6,4,0,8,4,8,1,7,0,8,4,3,7,9,9,6,5,3,7,8,6,6,6,4,2,0,2,2],
                 [4,5,0,3,0,8,7,4,8,5,7,1,2,1,5,0,1,6,5,0,2,3,9,3,0,4,8,3,0,5,9,8,2,4,7,6,1,3,6,6,4,9,9,6,2,9,4,5,6,5,8,8,7,1,5,1,8,0,1,6,3,7,0,2,9,2,8,0,4,5,9,2,3,3,7,7,7,0,4,4,6,1,6,3,1,7,1,8,3,5,6,2,7,8,9,4,2,2,9,9],
              ]:
    print(f'digits = {digits}')
    sol = Solution()
    r = sol.findEvenNumbers(digits)
    print(f'r = {r}')
    print('============================')

