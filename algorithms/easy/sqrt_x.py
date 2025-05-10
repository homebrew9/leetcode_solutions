import math

class Solution:
    def mySqrt(self, x: int) -> int:
        # Binary Search
        left, right = 0, 2**31 - 1
        while left <= right:
            mid = (left + right) // 2
            val = mid * mid
            if val == x:
                return mid
            if val > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

# Main section
for x in [
            4,
            8,
            0,
            2147483647,
            2147395600,
            398492824,
            101,
            1522756,
         ]:
    print(f'x = {x}')
    sol = Solution()
    r = sol.mySqrt(x)
    print(f'r = {r}')
    assert(int(math.sqrt(x)) == r)
    print('============================')

