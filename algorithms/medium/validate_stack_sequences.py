from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        N = len(pushed)
        i, j = 0, 0
        stack = list()
        while i < N and j < N:
            if pushed[i] == popped[j]:
                i += 1
                j += 1
                while stack and popped[j] == stack[-1]:
                    stack.pop()
                    j += 1
            elif pushed[i] < popped[j]:
                stack.append(pushed[i])
                i += 1
            else:
                if stack and popped[j] == stack[-1]:
                    stack.pop()
                    j += 1
                else:
                    stack.append(pushed[i])
                    i += 1
        while j < N:
            if popped[j] != stack [-1]:
                return False
            stack.pop()
            j += 1
        if len(stack) == 0:
            return True
        return False

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

