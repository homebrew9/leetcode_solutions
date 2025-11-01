class Solution:
    def smallestNumber(self, n: int) -> int:
        p = 1           # Start with p = 2**0 = 1
        while p <= n:
            p = p << 1  # Replace p by the next power of 2, until p is strictly greater than n
        return p - 1

# Main section
for n in [
            5,
            10,
            3,
            599,
            103,
            79,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.smallestNumber(n)
    print(f'r = {r}')
    print('=====================')


