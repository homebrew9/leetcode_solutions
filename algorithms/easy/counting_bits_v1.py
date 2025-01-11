from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # There is a pattern in the number of set bits.
        # If i = 2^p, then:
        #     res[i] = 1 + res[0]
        #     res[i+1] = 1 + res[1]
        #     res[i+2] = 1 + res[2]
        #     ...
        #     res[i+i-1] = 1 + res[i-1]
        if n < 1:
            return [n]
        powers = list()
        i = 0
        while (p := 2**i) <= n:
            powers.append(p)
            i += 1
        res = [0 for _ in range(n+1)]
        res[0] = 0
        for i in range(1, n+1):
            if i in powers:
                ptr = 0
            res[i] = 1 + res[ptr]
            ptr += 1
        return res

# Main section
for n in [
            0,
            1,
            2,
            3,
            4,
            5,
            100,
            267,
            7809,
            5314,
            35678,
            100000
         ]:
    sol = Solution()
    print(f'n = {n}')
    r = sol.countBits(n)
    print(f'r = {r}')
    print('=====================')

