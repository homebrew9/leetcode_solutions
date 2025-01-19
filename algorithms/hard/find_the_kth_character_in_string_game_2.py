from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        if k == 1:
            return 'a'
        N = len(operations)
        powers = [2**i for i in range(1, N+1)]
        powers = [0] + powers
        operations = [0] + operations
        #print(operations)
        #print(powers)
        N += 1
        total = 0
        for i in range(N - 1, 0, -1):
            #print(i, k, operations[i-1], operations[i])
            if powers[i-1] < k <= powers[i]:
                total += operations[i]
                k -= powers[i-1]
                if k <= 1:
                    break
        #print(total)
        return chr(97 + (total % 26))

# Main section
for k, operations, exp in [
                             (5, [0,0,0], 'a'),
                             (10, [0,1,0,1], 'b'),
                             (2, [1], 'b'),
                             (1, [1,0], 'a'),
                             (105, [1,0,1,1,1,0,0,1,0,1,0,0,0,1,1,0,0,0,1,0], 'b'),
                             (3599, [1,0,1,1,1,0,0,1,0,1,0,0,0,1,1,0,0,0,1,0], 'd'),
                             (98765, [1,0,1,1,1,0,0,1,0,1,0,0,0,1,1,0,0,0,1,0], 'd'),
                             (47387643, [0,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,0,0,1], 'f'),
                             (99048371, [0,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,0,0,1], 'h'),
                          ]:
    print(f'k, operations = {k}, {operations}')
    sol = Solution()
    r = sol.kthCharacter(k, operations)
    print(f'r = {r}')
    assert(r == exp)
    print('===================')


