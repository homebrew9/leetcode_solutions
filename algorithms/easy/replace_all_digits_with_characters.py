class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c, n):
            return chr(ord(c) + int(n))
        
        arr = list(s)
        for i, v in enumerate(arr):
            if i % 2 == 1:
                arr[i] = shift(arr[i-1], arr[i])
        return ''.join(arr)

# Main section
for s in [
            'a1c1e1',
            'a1b2c3d4e',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.replaceDigits(s)
    print(f'r = {r}')
    print('==========================')

