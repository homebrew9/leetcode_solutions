class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n).replace('0b','')
        max_val = 0
        pos = -1 
        while b.find('1', pos+1) >= 0:
            next_pos = b.find('1', pos+1)
            curr = next_pos - max(pos,0)
            max_val = max(max_val, curr)
            pos = next_pos
        return max_val

# Main section
for n in [
            22,
            8,
            5,
            12345678,
            99938235,
            65537,
            1048577,
            9876081,
            678,
            120,
            67,
            91,
            1,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.binaryGap(n)
    print(f'r = {r}')
    print('=============')


