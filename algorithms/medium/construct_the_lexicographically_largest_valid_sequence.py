# Use backtracking. The most important point to keep in mind is this:
# At a given index i of array "res", we try to fit integers from max to min. If we cannot fit
# an integer, we move to the next smaller one. Thus, backtrack function takes index i as parameter.
# As per the problem constraints, we will be always be able to construct a distanced sequence.
# If a suitable integer is found, then do the following:
#     1) add it to "used" set
#     2) update in the array "res"
# Then find the next open slot and call the recursive function. If this function returns False,
# then backtrack i.e. undo the steps 1) and 2) above. And move on to the next iteration.
#
from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        N = 2*n - 1
        res = [0 for _ in range(N)]
        used = set()   # nums already placed
        def backtrack(i):
            if i >= N:
                return True
            # Try largest elements
            for num in range(n, 0, -1):
                # Validation
                if num in used:
                    continue
                if num > 1 and (i + num >= N or res[i+num] > 0):
                    continue
                # We can add num at index i of res. Try decision.
                used.add(num)
                res[i] = num
                if num > 1:
                    res[i + num] = num
                # Fetch the next open slot
                j = i + 1
                while j < N and res[j] > 0:
                    j += 1
                # Recursive step
                if backtrack(j):
                    return True
                # Undo the work and backtrack
                used.remove(num)
                res[i] = 0
                if num > 1:
                    res[i + num] = 0
            return False
        backtrack(0)
        return res

# Main section
for n in [
            3,
            5,
            20,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.constructDistancedSequence(n)
    print(f'r = {r}')
    print('==========================')

