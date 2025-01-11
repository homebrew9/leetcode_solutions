class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def strSum(s):
            return str(sum([int(ch) for ch in s]))

        while len(s) > k:
            t = ''
            i = 0
            while i < len(s):
                t += strSum(s[i:i+k])
                i += k
            s = t
        return s

# Main section
for s, k in [
               ('11111222223', 3),
               ('00000000', 3),
               ('99999999999999999999999999999999999999999999999999999999999999999', 4),
            ]: 
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.digitSum(s, k)
    print(f'r = {r}')
    print('=========================')

