from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_val = 0
        max_val = 0
        num = 0
        for d in differences:
            num += d
            min_val = min(min_val, num)
            max_val = max(max_val, num)
        #print(min_val, max_val)
        diff = max_val - min_val
        return max((upper - lower + 1) - diff, 0)

# Main section
for differences, lower, upper in [
                                    ([1,-3,4], 1, 6),
                                    ([3,-4,5,1,-2], -4, 5),
                                    ([4,-7,2], 3, 6),
                                    ([3,4,8,6,-2,7,10,0,1,-8,-8,3,5,4,2,-9,8,-5,0,-7,5,2,5,5,-5,-8,-6,9,-1,8,0,-2,-10,-7,-1,-8,-1,1,1,2], 101, 199),
                                 ]:
    print(f'differences, lower, upper = {differences}, {lower}, {upper}')
    sol = Solution()
    r = sol.numberOfArrays(differences, lower, upper)
    print(f'r = {r}')
    print('=============================')

