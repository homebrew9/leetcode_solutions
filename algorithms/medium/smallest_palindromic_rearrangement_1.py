class Solution:
    def smallestPalindrome(self, s: str) -> str:
        N = len(s)
        if N == 1:
            return s
        arr1 = sorted(list(s[:N//2]))
        if N % 2 == 0:
            arr = arr1 + arr1[::-1]
        else:
            arr = arr1 + [s[N//2]] + arr1[::-1]
        return ''.join(arr)

# Main section
for s in [
            'z',
            'babab',
            'daccad',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.smallestPalindrome(s)
    print(f'r = {r}')
    print('========================')

