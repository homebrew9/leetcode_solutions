class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def is_leap(yr):
            is_leap_year = False
            if yr % 100 == 0:
                if yr % 400 == 0:
                    is_leap_year = True
                else:
                    is_leap_year = False
            elif yr % 4 == 0:
                is_leap_year = True
            return is_leap_year

        # We start with the knowledge that the epoch '1970-01-01' was a Thursday.
        # Then we find out the number of days between the epoch and specified date.
        week = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']
        mth_nonleap = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        mth_leap = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = 0
        # Days up to year-1
        for y in range(1970,year):
            if is_leap(y):
                days += 366
            else:
                days += 365
        # Days up to month-1
        for m in range(1, month):
            if m == 2 and is_leap(year):
                days += mth_leap[m]
                continue
            days += mth_nonleap[m]
        # Add up the days
        days += day - 1
        return week[days%7]

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


