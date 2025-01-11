from typing import List
from collections import defaultdict

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        d = defaultdict(int)
        d[rounds[0]] += 1
        for i in range(1, len(rounds)):
            sector = rounds[i-1]
            while True:
                sector += 1
                if sector > n:
                    sector -= n
                d[sector] += 1
                if sector == rounds[i]:
                    break
        max_val = max(d.values())
        arr = list()
        for k, v in d.items():
            if v == max_val:
                arr.append(k)
        return sorted(arr)

# Main section
for n, rounds in [
                    (4, [1,3,1,2]),
                    (2, [2,1,2,1,2,1,2,1,2]),
                    (7, [1,3,5,7]),
                 ]:
    print(f'n, rounds = {n}, {rounds}')
    sol = Solution()
    r = sol.mostVisited(n, rounds)
    print(f'r = {r}')
    print('=======================')

