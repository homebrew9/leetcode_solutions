from typing import List
import math

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def sieve(n):
            arr = [0 for _ in range(n+1)]
            for i in range(2, int(math.sqrt(n))+1):
                if arr[i] == 1:
                    continue
                arr[i] = 0
                for j in range(2*i, n+1, i):
                    arr[j] = 1
            arr = [i for i, v in enumerate(arr) if i > 1 and v == 0]
            self.primeSet = set(arr)
            return arr
        self.primeSet = set()
        arr = sieve(n)
        res = list()
        for i in range(len(arr)):
            #print(f'\ti, arr[i] = {i}, {arr[i]}')
            if n - arr[i] in self.primeSet and n - arr[i] > arr[i]:
                res.append([arr[i], n-arr[i]])
        #print(f'\t\tlen(arr) = {len(arr)}')
        #print(f'\t\t470453 is in set? : {470453 in self.primeSet}')
        #print(f'\t\t529547 is in set? : {529547 in self.primeSet}')
        #for i in range(len(arr)):
        #    if arr[i] == 470453:
        #        print(f'\t\t\tarr[{i}] = {arr[i]}')
        #        break
        #for i in range(len(arr)):
        #    if arr[i] == 529547:
        #        print(f'\t\t\tarr[{i}] = {arr[i]}')
        #        break
        #for i in sorted(list(self.primeSet)):
        #    print(f'\t\t\t{i}')
        return res

# Main section
for n in [
            1000000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.findPrimePairs(n)
    print(f'r = {r}')
    print('==================')

