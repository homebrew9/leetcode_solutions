class Solution:
    def fib(self, n: int) -> int:
        # iterative
        if n <= 1:
            return n
        n1 = 0
        n2 = 1
        for i in range(2,n+1):
            res = n1 + n2
            n1 = n2
            n2 = res
        return res

# Main section
for n in [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.fib(n)
    print(f'r = {r}')
    print('===========================')

