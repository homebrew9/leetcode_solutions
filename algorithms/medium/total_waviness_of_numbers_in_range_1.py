class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def get_waviness(n):
            if n <= 100:
                return 0
            s = str(n)
            N = len(s)
            waviness = 0
            for i in range(1, N-1):
                if (s[i-1] < s[i] and s[i] > s[i+1]) or (s[i-1] > s[i] and s[i] < s[i+1]):
                    waviness += 1
            return waviness
        res = 0
        for n in range(num1, num2 + 1):
            res += get_waviness(n)
        return res

# Main section
for num1, num2 in [
                     (120, 130),
                     (198, 202),
                     (4848, 4848),
                     (3519, 9076),
                  ]:
    print(f'num1, num2 = {num1}, {num2}')
    sol = Solution()
    r = sol.totalWaviness(num1, num2)
    print(f'r = {r}')
    print('===========================')


