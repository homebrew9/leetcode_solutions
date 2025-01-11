class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        n = abs(n)
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        if n == 1:
            return True
        else:
            return False

# Main solution
sol = Solution()
for n in [
397
2147483647
2
0
1
2
3
4
80
81
82
83
84
85
-397
-2147483648
-2
-1
-2
-3
-4
-80
-81
-82
-83
-84
-85
         ]:
    print(f'n = {n}')
    r = sol.isUgly(n)
    print(f'r = {r}')
    print('============================')


