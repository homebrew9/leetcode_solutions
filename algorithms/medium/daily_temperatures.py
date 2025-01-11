from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        size = len(temperatures)
        res = [0 for _ in range(size)]
        for i, v in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < v:
                ind = stack.pop()
                res[ind] = i - ind
            stack.append(i)
        return res

# Main section
for temperatures in [
                       #[73,74,75,71,69,72,76,73],
                       #[30,40,50,60],
                       #[30,60,90],
                       [1,1,2,1,5],
                    ]:
    print(f'temperatures = {temperatures}')
    sol = Solution()
    r = sol.dailyTemperatures(temperatures)
    print(f'r = {r}')
    print('=============================')

