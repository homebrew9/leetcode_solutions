class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # n <= 20 so brute force should work here
        hsh = {'1': '0', '0': '1'}
        i = 1
        s = '0'
        while i < n:
            s = s + '1' + ''.join([hsh[ch] for ch in s][::-1])
            i += 1
        return s[k-1]

# Main section
for n, k in [
               (3, 1),
               (4, 11),
               (20, 32759),
            ]:
    print(f'n, k = {n}, {k}')
    sol = Solution()
    r = sol.findKthBit(n, k)
    print(f'r = {r}')
    print('=================================================')
 















