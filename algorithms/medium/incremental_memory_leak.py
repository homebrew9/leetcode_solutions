from typing import List

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 0
        while True:
            i += 1
            if memory1 < i and memory2 < i:
                return [i, memory1, memory2]
            if memory1 >= memory2:
                memory1 -= i
            else:
                memory2 -= i

# Main section
for memory1, memory2 in [
                           (2, 2),
                           (8, 11),
                           (1234567890, 2147483647),
                           (0, 0),
                           (0, 10),
                        ]:
    print(f'memory1, memory2 = {memory1}, {memory2}')
    sol = Solution()
    r = sol.memLeak(memory1, memory2)
    print(f'r = {r}')
    print('===============================')


