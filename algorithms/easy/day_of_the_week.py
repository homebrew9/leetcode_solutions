from datetime import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime(year,month,day).strftime('%A')

# Main section
for day, month, year in [
                           (31, 8, 2019),
                           (18, 7, 1999),
                           (15, 8, 1993),
                           (15, 9, 2022),
                        ]:
    print(f'day, month, year = {day}, {month}, {year}')
    sol = Solution()
    r = sol.dayOfTheWeek(day, month, year)
    print(f'r = {r}')
    print('===========================')

