from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Go from left to right and keep on pushing the indexes to stack as
        # long as temperatures are non-increasing. Once a particular
        # temperature is high, keep popping and resetting the index difference
        # as  long as the temps in the stack are lower (or the stack is non-empty).
        stack = list()
        N = len(temperatures)
        res = [0 for _ in range(N)]
        for i, v in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < v:
                ind = stack.pop()
                res[ind] = i - ind
            stack.append(i)
        return res

# Main section
for temperatures in [
                       [73,74,75,71,69,72,76,73],
                       [30,40,50,60],
                       [30,60,90],
                       [31,31,32,31,35],
                       [37,31,32,31,39],
                    ]:
    print(f'temperatures = {temperatures}')
    sol = Solution()
    r = sol.dailyTemperatures(temperatures)
    print(f'r = {r}')
    print('==================')

