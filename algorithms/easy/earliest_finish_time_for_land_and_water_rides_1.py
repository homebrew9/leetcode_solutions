from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # Plan 1: Earliest land ride + most appropriate water ride
        # Plan 2: Earliest water ride + most appropriate land ride
        # Return min time from Plan 1 and Plan 2
        # ==== Plan 1 ====
        min_land_time = min([(t + d) for t, d in zip(landStartTime, landDuration)])
        res1 = min([max(t, min_land_time) + d for t, d in zip(waterStartTime, waterDuration)])
        # ==== Plan 2 ====
        min_water_time = min([(t + d) for t, d in zip(waterStartTime, waterDuration)])
        res2 = min([max(t, min_water_time) + d for t, d in zip(landStartTime, landDuration)])
        return min(res1, res2)

# Main section
for landStartTime, landDuration, waterStartTime, waterDuration in [
         ([2,8], [4,1], [6], [3]),
         ([5], [3], [1], [10]),
         ([82,8,51], [58,47,64], [13,22], [13,75]),
    ]:
    print(f'landStartTime  = {landStartTime}')
    print(f'landDuration   = {landDuration}')
    print(f'waterStartTime = {waterStartTime}')
    print(f'waterDuration  = {waterDuration}')
    sol = Solution()
    r = sol.earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration)
    print(f'r = {r}')
    print('==============================')



















