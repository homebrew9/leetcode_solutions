from typing import List
from collections import Counter

class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        cntr = Counter(nums)
        key_list = sorted(cntr.keys())
        if len(key_list) < k:
            return False
        if len(key_list) >= k and max(cntr.values()) == 1:
            return True
        k1 = k
        for key in key_list:
            cntr[key] -= 1
            if cntr[key] == 0:
                del cntr[key]
            k1 -= 1
            if k1 == 0:
                break
        if len(cntr) == 0 or (sum(cntr.values()) >= k and max(cntr.values()) <= 2):
            return True
        return False

# Main section
for nums, k in [
                  ([1,2,2,3,3,4,4], 3),
                  ([5,6,6,7,8], 3),
                  ([1,2,3,4,5,6,7,7,8,8], 5),
                  ([1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10], 9),
                  ([1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10], 10),
                  ([132,1059,2956,5482,7286,7401,7735,9018,9927,10754,12140,12316,13656,15070,15616,15955,19164,19526,20875,23161,25223,25541,29133,30969,31070,31810,31886,33286,33536,34671,35339,36680,36931,37499,37834,38435,39559,40182,41142,43813,46242,46655,46948,49380,51159,52673,54714,57119,61608,63901,65550,66002,66073,66127,66865,66866,67206,67579,68575,70292,71256,77362,77842,79428,79545,79595,81729,84060,85570,86592,88968,89703,89801,90085,90843,92517,96536,98085,99213,99401], 75),
                  ([3084,15321,18763,36395,42996,45760,49337,82060,91390,91585], 1),
                  ([4283,9121,57996,60116,81660], 5),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.canDivideIntoSubsequences(nums, k)
    print(f'r = {r}')
    print('=============================')

