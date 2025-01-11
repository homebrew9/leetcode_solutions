from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [None for _ in range(N)]
        stack = list()
        for i in range(N-1, -1, -1):
            tcur = temperatures[i]
            #print(f'\ti, tcur, stack, res = {i}, {tcur}, {stack}, {res}')
            if len(stack) == 0:
                stack.append(i)
                res[i] = 0
            elif tcur < temperatures[stack[-1]]:
                res[i] = stack[-1] - i
                stack.append(i)
            else:
                while stack:
                    itop = stack[-1]
                    ttop = temperatures[itop]
                    if tcur < ttop:
                        res[i] = itop - i
                        stack.append(i)
                        break
                    else:
                        stack.pop()
                if not stack:
                    res[i] = 0
                    stack.append(i)
        return res

# Main section
for temperatures in [
                       [73,74,75,71,69,72,76,73],
                       [30,50,35,35,70],
                       [30,90,35,35,70],
                    ]:
    print(f'temperatures = {temperatures}')
    sol = Solution()
    r = sol.dailyTemperatures(temperatures)
    print(f'r = {r}')
    print('===============')

