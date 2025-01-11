#
# Ref: https://leetcode.com/problems/binary-watch/discuss/2428153/Simple-python-solution.-98-faster
# User: trpaslik
#
from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        arr_times = list()
        # Store the bitcounts of all binary numbers from 0..59
        # in an array
        arr_bitcount = [bin(i).count('1') for i in range(60)]
        # Hour range is 0..11 and minute range is 0..59. For these ranges,
        # determine hour_bitcount and min_bitcount, add them and equate to
        # turnedOn. For example - if the time is 10:38 then
        # 10 = 1010(bin)   => bitcount = 2, and
        # 38 = 100110(bin) => bitcount = 3
        # Hence, 2 LEDs (8, 2) from the Hour panel and 3 LEDs (32, 4, 2) from
        # the Minute panel will be turned on in the Binary Watch.
        for h in range(12):
            hb = arr_bitcount[h]
            for m in range(60):
                hm = arr_bitcount[m]
                if hb + hm == turnedOn:
                    arr_times.append(str(h)+':'+'%02d'%(m))
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


