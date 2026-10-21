from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(start: int, current_combination: list[int]):
            # If the combination is done
            if len(current_combination) == k:
                result.append(list(current_combination))
                return
            # Optimization: Only loop if there are enough remaining numbers to fill k slots
            # Remaining slots needed = k - len(current_combination)
            # Max start index possible = n - (k - len(current_combination)) + 1
            for i in range(start, n - (k - len(current_combination)) + 2):
                # Add i into the current combination
                current_combination.append(i)
                # Move on to the next element
                backtrack(i + 1, current_combination)
                # Backtrack, remove i from current combination
                current_combination.pop()
        backtrack(1, [])
        return result


# Main section
for n, k in [
               (4, 2),
               (1, 1),
               (9, 5),
            ]:
    print(f'n, k = {n}, {k}')
    sol = Solution()
    r = sol.combine(n, k)
    print(f'r = {r}')
    print('===================================')


















