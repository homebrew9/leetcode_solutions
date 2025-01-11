class Solution:
    def replaceDigits(self, s: str) -> str:
        chars = [chr(i) for i in range(97,123)]
        arr = list(s)
        for i, v in enumerate(arr):
            if i % 2 == 1:
                arr[i] = chars[ord(arr[i-1]) - 97 + int(arr[i])]
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

