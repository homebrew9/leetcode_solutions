class Solution:
    def climbStairs(self, n: int) -> int:
        def numberOfWays(n):
            if n <= 1:
                arr[n] = 1
                return arr[n]
            if not arr[n] is None:
                return arr[n]
            one_way = numberOfWays(n-1)
            arr[n-1] = one_way
            two_way = numberOfWays(n-2)
            arr[n-2] = two_way
            arr[n] = arr[n-1] + arr[n-2]
            return arr[n]

        arr = [None] * 46
        arr[0] = 1
        res = numberOfWays(n)
        #print(f'\tarr = {arr}')
        return res
        
# Main section
for n in [
            45
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.climbStairs(n)
    print(f'r = {r}')
    print('=================')

