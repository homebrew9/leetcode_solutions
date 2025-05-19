class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i, v in enumerate(s):
            res += (i + 1) * (123 - ord(v))
        return res

# Main section
for s in [
            'abc',
            'zaza',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.reverseDegree(s)
    print(f'r = {r}')
    print('============================')




