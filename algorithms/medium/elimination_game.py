class Solution:
    def lastRemaining(self, n: int) -> int:
        # Using recursive function
        def solve(min_val, max_val, step, direction):
            if max_val <= min_val:
                return min_val
            if direction == 'right':
                if (max_val - min_val) % (2 * step) == 0:
                    # min_val will be removed!
                    min_val = min_val + step
                max_val = max_val - step
            else:
                if (max_val - min_val) % (2 * step) == 0:
                    # max_val will be removed!
                    max_val = max_val - step
                min_val = min_val + step
            direction = 'right' if direction == 'left' else 'left'
            return solve(min_val, max_val, 2*step, direction)
        min_val = 1
        max_val = n
        step = 1
        direction = 'left'
        return solve(min_val, max_val, step, direction)

# Main section
for n in [
            1,
            2,
            3,
            4,
            5,
            89,
            187,
            190,
            2536,
            67483,
            48783,
            8885945,
            8372873,
            9988664,
            1000000,
            1000000000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.lastRemaining(n)
    print(f'r = {r}')
    print('===============')

