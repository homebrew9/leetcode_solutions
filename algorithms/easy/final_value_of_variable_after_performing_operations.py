from typing import List
from functools import reduce

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        hsh = {'++X': 1, 'X++': 1, '--X': -1, 'X--': -1}
        res = 0
        for op in operations:
            res += hsh[op]
        return res

    def finalValueAfterOperations_1(self, operations: List[str]) -> int:
        hsh = {'++X': 1, 'X++': 1, '--X': -1, 'X--': -1}
        return reduce(lambda x,y: x+y, [hsh[o] for o in operations])

# Main section
for operations in [
                     ['--X','X++','X++'],
                     ['++X','++X','X++'],
                     ['X++','++X','--X','X--'],
                  ]:
    print(f'operations = {operations}')
    sol = Solution()
    r = sol.finalValueAfterOperations(operations)
    r1 = sol.finalValueAfterOperations(operations)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('=====================')







