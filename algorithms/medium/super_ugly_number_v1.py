from typing import List
import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        while n:
            node = heapq.heappop(heap)
            while heap and node == heap[0]:
                heapq.heappop(heap)
            for i in primes:
                heapq.heappush(heap, i * node)
            n = n - 1
        return node

# Main section
for n, primes in [
                    (12, [2,7,13,19]),
                    (1, [2,3,5]),
                    (64, [2,5,7,11,13,17,19]),
                    (100000, [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]),
                 ]:
    print(f'n, primes = {n}, {primes}')
    sol = Solution()
    r = sol.nthSuperUglyNumber(n, primes)
    print(f'r = {r}')
    print('==================')

