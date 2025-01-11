#
# Elegant algorithm by lee215
#
from typing import List

class Solution:
    #def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    #    N = len(pushed)
    #    stack = list()
    #    i = 0
    #    for x in pushed:
    #        stack.append(x)
    #        while stack and i < N:
    #            if popped[i] == stack[-1]:
    #                stack.pop()
    #            i += 1
    #    return len(stack) == 0
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = list()
        i = 0
        for x in pushed:
            stack.append(x)
            while stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return len(stack) == 0

# Main section
for pushed, popped in [
                         ([1,2,3,4,5], [4,5,3,2,1]),
                         ([1,2,3,4,5], [4,3,5,1,2]),
                      ]:
    print(f'pushed, popped = {pushed}, {popped}')
    sol = Solution()
    r = sol.validateStackSequences(pushed, popped)
    print(f'r = {r}')
    print('=====================')


