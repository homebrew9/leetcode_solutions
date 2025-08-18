class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        for i in range(len(s)):
            if s[i] == '6':
                return int(s[:i] + '9' + s[i+1:])
        return num

# Main section
for num in [
              9669,
              9996,
              9999,
           ]:
    print(f'num = {num}')
    sol = Solution()
    r = sol.maximum69Number(num)
    print(f'r   = {r}')
    print('==============================')

