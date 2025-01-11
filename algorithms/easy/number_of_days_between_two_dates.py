class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def isLeapYear(year):
            is_leap = False
            if year % 100 == 0:
                if year % 400 == 0:
                    is_leap = True
            elif year % 4 == 0:
                is_leap = True
            return is_leap

        def daysSinceEpoch(s):
            year = int(s[:4])
            month = int(s[5:7])
            day = int(s[8:])
            non_leap_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
            leap_days     = [0,31,29,31,30,31,30,31,31,30,31,30,31]
            total = 0
            for y in range(1971, year):
                if isLeapYear(y):
                    total += sum(leap_days)
                else:
                    total += sum(non_leap_days)
            for m in range(1, month):
                if isLeapYear(year):
                    total += leap_days[m]
                else:
                    total += non_leap_days[m]
            total += day
            return total

        days1 = daysSinceEpoch(date1)
        days2 = daysSinceEpoch(date2)
        return abs(days1 - days2)

# Main section
for date1, date2 in [
                       ('2019-06-29', '2019-06-30'),
                       ('2020-01-15', '2019-12-31'),
                       ('1971-01-01', '2100-12-31'),
                       ('2022-01-01', '2022-01-01'),
                    ]: 
    print(f'date1, date2 = {date1}, {date2}')
    sol = Solution()
    r = sol.daysBetweenDates(date1, date2)
    print(f'r = {r}')
    print('=========================')

