from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        def isInt(n):
            try:
                n_test = int(n)
            except:
                return False
            return True
        
        ops = []
        for i in operations:
            if isInt(i):
                ops.append(int(i))
            elif i == '+':
                ops.append(ops[-1] + ops[-2])
            elif i == 'D':
                ops.append(2*ops[-1])
            elif i == 'C':
                ops.pop()
        return sum(ops)

# Main section
for operations in [
                     ['5','2','C','D','+'],
                     ['5','-2','4','C','D','9','+','+'],
                     ['1','C'],
                  ]:
    print(f'operations = {operations}')
    sol = Solution()
    r = sol.calPoints(operations)
    print(f'r = {r}')
    print('=================')

