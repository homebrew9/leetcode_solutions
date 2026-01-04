class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        # Type A patterns (RYG, RGY, YRG, YGR, GRY, GYR): 6 total
        # Type B patterns (RYR, RGR, YRY, YGY, GRG, GYG): 6 total
        # 
        # Transition rules:
        # From a Type A row, you can create 2 Type A and 2 Type B valid next rows
        # From a Type B row, you can create 2 Type A and 3 Type B valid next rows
        # 
        # This gives us the recurrence relations:
        # new_dpA = 2 * dpA + 2 * dpB
        # new_dpB = 2 * dpA + 3 * dpB
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # For row 1: 6 Type A patterns + 6 Type B patterns = 12 total
        dpA, dpB = 6, 6
        
        # Start from row 2 to row n
        for i in range(2, n + 1):
            new_dpA = (2 * dpA + 2 * dpB) % MOD
            new_dpB = (2 * dpA + 3 * dpB) % MOD
            dpA, dpB = new_dpA, new_dpB
        
        return (dpA + dpB) % MOD

# Main section
for n in [
            1,
            10,
            50,
            100,
            1000,
            2500,
            5000,
        ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.numOfWays(n)
    print(f'r = {r}')
    print('========================')



