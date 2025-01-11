class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Use binary search. In the series of numbers [1..n], find
        # greatest k such that k*(k+1)/2 is less than n
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            curr = (mid * (mid + 1))//2
            if curr == n:
                return mid
            elif curr > n:
                high = mid - 1
            else:
                low = mid + 1
        return high

# Main section
for n in [
            5,
            8,
            26,
            1,
            3,
            6,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            59
         ]:
    sol = Solution()
    print(f'n = {n}')
    r = sol.arrangeCoins(n)
    print(f'r = {r}')
    print('==========================')



