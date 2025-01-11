class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def fetchBit(n, k):
            if n == 1:
                return 0
            k1 = k // 2
            if  k == k1*2 + 1 and fetchBit(n-1, k1) == 1:
                return 0
            elif k == k1*2 and fetchBit(n-1, k1) == 0:
                return 0
            elif k == k1*2 and fetchBit(n-1, k1) == 1:
                return 1
            elif k == k1*2 + 1 and fetchBit(n-1, k1) == 0:
                return 1
        return fetchBit(n, k-1)

# Main section
for n, k in [
               (1, 1),
               (2, 1),
               (2, 2),
               (5, 9),
               (30, 123456),
               (28, 9987),
               (28, 100100),
               (25, 456),
               (20, 8765),
            ]:
    print(f'n, k = {n}, {k}')
    sol = Solution()
    r = sol.kthGrammar(n, k)
    print(f'r = {r}')
    print('===================')

