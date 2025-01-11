class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n).replace('0b','')
        max_val = 0
        curr = 0
        pos = 0
        prev_pos = pos
        while b.find('1', pos) >= 0:
            next_pos = b.find('1', pos)
            curr = next_pos - prev_pos
            max_val = max(max_val, curr)
            prev_pos = next_pos
            pos = next_pos + 1
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

