import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Using binary search, credit goes to "wingkwong"
        max_int = 2**31 - 1
        left = 0
        right = int(math.log10(max_int) / math.log10(3))
        while left < right:
            middle = int((left + right)/2)
            guess = 3**middle
            if n > guess:
                # Very important to skip middle, otherwise it could go into an infinite loop
                left = middle + 1
            else:
                right = middle
        # At this point, the while loop is over and we have a value of left,
        # but we don't know if it is a power of 3
        return 3**left == n

# Main section
sol = Solution()
for n in [
            -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 59049, 59099, -59049, -59099, 1162261467, -1162261467, 1162261999
         ]:
    print(f'n = {n}')
    r = sol.isPowerOfThree(n)
    print(f'r = {r}')
    print('===========================')





