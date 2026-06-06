from collections import defaultdict

class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        hsh = defaultdict(int)
        streak = 0
        for b in bin(n)[2:]:
            if b == '1':
                streak += 1
            else:
                if streak > 0:
                    hsh[streak] += 1
                streak = 0
        if streak > 0:
            hsh[streak] += 1
        for k, v in hsh.items():
            if k > 2:
                return False
        return 2 in hsh and hsh[2] == 1

# Main section
for n in [
            3,
            7,
            12,
            45,
            35,
            111,
            15,
            31,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.consecutiveSetBits(n)
    print(f'r = {r}')
    print('==============================')




