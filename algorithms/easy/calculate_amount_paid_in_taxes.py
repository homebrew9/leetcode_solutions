from typing import List

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        total_tax = 0
        leftover = float('inf')
        for i, bracket in enumerate(brackets):
            if leftover == 0:
                break
            if i == 0:
                if bracket[0] < income:
                    taxable_income = bracket[0]
                    leftover = income - taxable_income
                else:
                    taxable_income = income
                    leftover = 0
            else:
                taxable_income = bracket[0] - brackets[i-1][0]
                if taxable_income < leftover:
                    leftover = leftover - taxable_income
                else:
                    taxable_income = leftover
                    leftover = 0
            total_tax += taxable_income * bracket[1]/100
            #print(f'\ttotal_tax = {total_tax}')
        return total_tax

# Main section
for brackets, income in [
                           ([[3,50],[7,10],[12,25]], 10),
                           ([[1,0],[4,25],[5,50]], 2),
                           ([[2,50]], 0),
                           ([[3,50],[7,10],[12,25]], 0),
                           ([[3,50],[7,10],[12,25]], 1),
                           ([[3,50],[7,10],[12,25]], 2),
                           ([[3,50],[7,10],[12,25]], 3),
                           ([[3,50],[7,10],[12,25]], 4),
                           ([[3,50],[7,10],[12,25]], 5),
                           ([[3,50],[7,10],[12,25]], 6),
                           ([[3,50],[7,10],[12,25]], 7),
                           ([[3,50],[7,10],[12,25]], 8),
                           ([[3,50],[7,10],[12,25]], 9),
                           ([[3,50],[7,10],[12,25]], 10),
                           ([[3,50],[7,10],[12,25]], 11),
                           ([[3,50],[7,10],[12,25]], 12),
                        ]:
    print(f'brackets, income = {brackets}, {income}')
    sol = Solution()
    r = sol.calculateTax(brackets, income)
    print(f'r = {r}')
    print('================')

