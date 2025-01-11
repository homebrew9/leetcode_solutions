class Solution:
    # Recursive, highly inefficient
    #def climbStairs(self, n: int) -> int:
    #    def waysToClimb(n):
    #        if n <= 2:
    #            return n
    #        return waysToClimb(n-1) + waysToClimb(n-2)
    #    return waysToClimb(n)

    # Recursive, memoized
    def climbStairs(self, n: int) -> int:
        def waysToClimb(n):
            if self.steps[n] != -1:
                return self.steps[n]
            self.steps[n] = waysToClimb(n-1) + waysToClimb(n-2)
            return self.steps[n]

        if n <= 2:
            return n
        self.steps = [-1 for _ in range(n+1)]
        self.steps[0] = 0
        self.steps[1] = 1
        self.steps[2] = 2
        return waysToClimb(n)

# Main section
for n in [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            15,
            20,
            25,
            30,
            35,
            40,
            45,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.climbStairs(n)
    print(f'r = {r}')
    print('=================')


