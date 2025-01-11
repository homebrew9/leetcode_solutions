class Solution:
    def fib(self, n: int) -> int:
        # recursive, memoized
        def fib_memoized(n):
            if n < len(arr):
                return arr[n]
            arr.append(fib_memoized(n-1) + fib_memoized(n-2))
            return arr[n]

        arr = [0, 1]
        return fib_memoized(n)

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


