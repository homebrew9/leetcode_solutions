#
# Wrong algorithm! Does not work for 5610 (expected 6015, got 6510)
#
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        def nextInt(lst, i, j):
            lst[j], lst[i] = lst[i], lst[j]
            return int(''.join(lst))

        if n < 10:
            return -1
        arr = list(str(n))
        for i in range(len(arr) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                next_int = nextInt(arr, i, j)
                #print(f'\ti, j, next_int = {i}, {j}, {next_int}')
                if next_int > n:
                    return next_int
        return -1

# Main section
for n in [
            12,
            21,
            12345,
            5106,
            5160,
            5601,
            5610,
            4321,
            432,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.nextGreaterElement(n)
    print(f'r = {r}')
    print('================')

