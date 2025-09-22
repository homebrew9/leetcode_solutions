from typing import List

class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        def get_penalty(days):
            if days == 1:
                return 1
            if 2 <= days <= 5:
                return 2 * days
            return 3 * days
        return sum(map(get_penalty, daysLate))

# Main section
for daysLate in [
                   [5,1,7],
                   [1,1],
                ]:
    print(f'daysLate = {daysLate}')
    sol = Solution()
    r = sol.lateFee(daysLate)
    print(f'r = {r}')
    print('===================')

