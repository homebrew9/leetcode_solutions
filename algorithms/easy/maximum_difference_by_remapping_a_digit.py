class Solution:
    def minMaxDifference(self, num: int) -> int:
        # Max : Find the leftmost digit other than 9 and remap that to 9.
        # Min : Find the leftmost digit other than 0 and remap that to 0.
        s = str(num)
        digit = None
        max_num, min_num = num, num
        for ch in s:
            if ch != '9':
                digit = ch
                break
        if digit is not None:
            max_num = int(s.replace(digit, '9'))
        digit = None
        for ch in s:
            if ch != '0':
                digit = ch
                break
        if digit is not None:
            min_num = int(s.replace(digit, '0'))
        return max_num - min_num

# Main section
for num in [
              11891,
              90,
              1000990,
              347391,
              759374,
              100000000,
              9999,
           ]:
    print(f'num = {num}')
    sol = Solution()
    r = sol.minMaxDifference(num)
    print(f'r  = {r}')
    print('===================')













