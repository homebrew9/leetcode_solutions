from typing import List
from itertools import combinations, product

# It's unclear to me as to why "12:00" is not a valid time!
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn == 0:
            return ['0:00']
        arr_times = list()
        arr_all_hours = [8,4,2,1]
        arr_all_mins = [32,16,8,4,2,1]
        arr_hr = list()
        arr_min = list()
        for h in range(0,5):
            for m in range(0,7):
                if h+m == turnedOn:
                    print(h,m)
                    if h > 0:
                        for i in combinations(arr_all_hours, h):
                            # "12:00" is not a valid time! Hence use < instead of <=
                            if sum(i) < 12:
                                arr_hr.append(sum(i))
                        if len(arr_hr) == 0:
                            arr_min = []
                            break
                    if m > 0:
                        for j in combinations(arr_all_mins, m):
                            if sum(j) <= 59:
                                arr_min.append(sum(j))
                        if len(arr_min) == 0:
                            arr_hr = []
                            break
                    if len(arr_hr) == 0 and len(arr_min) == 0:
                        return arr_times
                    elif len(arr_hr) > 0 and len(arr_min) > 0:
                        for i in product(arr_hr, arr_min):
                            arr_times.append(str(i[0]) + ':' + '%02d'%(i[1]))
                    elif len(arr_hr) == 0:
                        for minute in arr_min:
                            arr_times.append('0:' + '%02d'%(minute))
                    else:
                        for hour in arr_hr:
                            arr_times.append(str(hour) + ':00')
                    print(f'\tarr_hr    = {arr_hr}')
                    print(f'\tarr_min   = {arr_min}')
                    print(f'\tarr_times = {arr_times}')
                    arr_hr = []
                    arr_min = []
        return arr_times

# Main section
sol = Solution()
for t in [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
         ]:
    print(f't = {t}')
    r = sol.readBinaryWatch(t)
    print(f'r = {r}')
    print('======================')


