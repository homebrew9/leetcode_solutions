class Solution:
    def lastRemaining(self, n: int) -> int:
        # Using iteration
        min_val = 1
        max_val = n
        step = 1
        direction = 'left'
        while min_val < max_val:
            if direction == 'right':
                if (max_val - min_val) % (2 * step) == 0:
                    # min_val will be removed!
                    min_val += step
                max_val -= step
            else:
                if (max_val - min_val) % (2 * step) == 0:
                    # max_val will be removed!
                    max_val -= step
                min_val += step
            # Reverse the direction
            direction = 'right' if direction == 'left' else 'left'
            # Double the step
            step *= 2
        return min_val

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

