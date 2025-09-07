from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        for i in range(1, n//2 + 1):
            arr += [i, -i]
        if n % 2 == 1:
            arr += [0]
        return arr
    def sumZero_1(self, n: int) -> List[int]:
        is_odd = n % 2
        res = list()
        if is_odd:
            res.append(0)
            n -= 1
        k = 1
        for _ in range(0,n,2):
            res.extend([-k, k])
            k += 1
        return res
    def sumZero_2(self, n: int) -> List[int]:
        return list(range(1,n)) + [n*(1-n)//2]
 
# Main section
for n in [
            1,
            2,
            3,
            4,
            5,
            20,
            57,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.sumZero(n)
    r1 = sol.sumZero_1(n)
    r2 = sol.sumZero_2(n)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print(f'r : (len, sum) = ({len(r)}, {sum(r)}) \nr1: (len, sum) = ({len(r1)}, {sum(r1)}) \nr2: (len, sum) = ({len(r2)}, {sum(r2)})  ')
    print('===================')



















