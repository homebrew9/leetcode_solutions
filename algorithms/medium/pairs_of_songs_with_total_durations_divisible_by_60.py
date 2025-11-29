from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = [0] * 60
        res = 0
        for t in time:
            r = t % 60
            # Find complement remainder
            complement = (60 - r) % 60
            res += count[complement]
            count[r] += 1
        return res

# Main section
for time in [
               [30,20,150,100,40],
               [60,60,60],
            ]:
    print(f'time = {time}')
    sol = Solution()
    r = sol.numPairsDivisibleBy60(time)
    print(f'r = {r}')
    print('===========================')




