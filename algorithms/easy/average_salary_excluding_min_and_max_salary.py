from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        sum_sal = 0
        min_sal = 10**6 + 1
        max_sal = 0
        for sal in salary:
            sum_sal += sal
            if sal < min_sal:
                min_sal = sal
            if sal > max_sal:
                max_sal = sal
        # Now calculate the average of sum_sal - min - max
        sum_sal -= min_sal
        sum_sal -= max_sal
        cnt = len(salary) - 2
        return (sum_sal/cnt)

# Main section
for salary in [
                 [4000,3000,1000,2000],
                 [1000,2000,1500],
                 [1000,5000,4333,1287,6000],
                 [1000,1234,5678,9012,3456,4567,1001],
              ]:
    print(f'salary = {salary}')
    sol = Solution()
    r = sol.average(salary)
    print(f'r = {r}')
    print('==============')

