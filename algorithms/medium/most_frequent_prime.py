
from typing import List
import math
from collections import defaultdict


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        def sieve(n):
            arr = [1 for _ in range(n+1)]
            lim = int(math.sqrt(n))
            for i in range(2, lim+1):
                if arr[i] == 1:
                    for j in range(2*i, n+1, i):
                        arr[j] = 0
            self.primes = set([i for i, v in enumerate(arr) if i >=2 and v == 1])
        self.primes = set()
        sieve(1000000)
        rows = len(mat)
        cols = len(mat[0])
        directions = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
        hsh = defaultdict(int)
        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    row, col = r, c
                    curr = str(mat[r][c])
                    #print(f'\trow, col, curr = {row}, {col}, {curr}')
                    #print(f'\t\tdr, dc = {dr}, {dc}')
                    while True:
                        rnew, cnew = row + dr, col + dc
                        #print(f'\t\t\trnew, cnew = {rnew}, {cnew}')
                        if 0 <= rnew < rows and 0 <= cnew < cols:
                            curr += str(mat[rnew][cnew])
                            #print(f'\t\t\t\tcurr = {curr}')
                            if int(curr) > 10 and int(curr) in self.primes:
                                #print(f'\t\t\t\t\tinside if : curr = {curr}')
                                hsh[int(curr)] += 1
                        else:
                            break
                        row, col = rnew, cnew
        #print(hsh)
        if len(hsh) == 0:
            return -1
        max_val = max(hsh.values())
        res = float('-inf')
        for k, v in hsh.items():
            if v == max_val:
                res = max(res, k)
        return res

for mat in [
              #[[1,1],[9,9],[1,1]],
              #[[7]],
              #[[9,7,8],[4,6,5],[2,8,6]],
              #[[7,3,3,9,2,4],[3,3,3,7,6,8],[1,7,2,2,7,8],[6,5,6,5,2,8],[4,2,5,3,5,4],[1,1,6,9,8,7]],
              #[[4,3,6,6,6,2],[4,6,4,9,7,8],[8,5,1,8,6,6],[4,4,6,6,9,2],[4,6,4,3,2,4],[6,2,1,6,7,9]],
              #[[2,1,8,9,5,5],[5,5,2,5,5,6],[8,5,5,1,7,6],[3,2,6,9,3,8],[8,1,5,3,4,8],[7,4,7,4,4,8]],
              #[[1,2,5,1,2,1],[2,2,4,3,9,3],[7,7,2,5,4,3],[5,9,8,2,2,4],[3,5,6,7,6,8],[1,2,4,6,6,4]],
              #[[4,8,1,7,3,5],[2,3,9,3,7,1],[8,3,7,7,8,1],[1,5,2,4,9,3],[6,3,9,7,7,2],[7,6,1,2,2,6]],
              [[4,4,5]],
           ]:
    print(f'mat = {mat}')
    sol = Solution()
    r = sol.mostFrequentPrime(mat)
    print(f'r = {r}')
    print('========================')







