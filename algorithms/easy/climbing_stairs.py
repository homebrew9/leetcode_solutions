class Solution:
    def climbStairs(self, n: int) -> int:
        def stepCount(n):
            #print(f'\tn = {n} ; steps = {steps}')
            if len(steps) >= n + 1:
                return steps[n]
            #if n <= 2:
            #    steps[n] = n
            #    return steps[n]
            steps.append(stepCount(n-1) + stepCount(n-2))
            #print(f'\t\tsteps = {steps}')
            return steps[n]
        
        if n <= 2:
            return n
        steps = [0,1,2]
        ans = stepCount(n)
        return ans

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
    print('==========================')

