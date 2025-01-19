from typing import List
import functools

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # The most important intuition is the following:
        # Both the original arrays below map to the same derived array:
        #     original_1 = [1, 0, 1, 0, 1, 0]
        #     original_2 = [0, 1, 0, 1, 0, 1]
        # That's because if we flip the bits of two operands then the output of
        # XOR operation stays the same! 0^1 = 1^0 and 0^0 = 1^0
        N = len(derived)
        original = [None for _ in range(N)]
        # Let's start with an assumption that the first element in the
        # original list is 0 and see if we can XOR our way till the end!
        original[0] = 0
        for i in range(1, N):
            original[i] = original[i-1] ^ derived[i-1]
        return original[N-1] ^ derived[N-1] == original[0]

    def doesValidArrayExist_1(self, derived: List[int]) -> bool:
        # A functional approach to deriving the XOR of entire list.
        # We return True if the XOR of the list equals 0.
        return functools.reduce(lambda x,y: x^y, derived) == 0

# Main section
for derived in [
                  [1,1,0],
                  [1,1],
                  [1,0],
                  [1,0,1,1,1],
                  [0,1,1,1,1],
                  [0,1,1,1,0],
                  [1,1,0,1,1],
                  [0,1,1,0,1,1,0,0,0,1,1,0,1,0,0,0,1,1,1,0],
               ]:
    print(f'derived = {derived}')
    sol = Solution()
    r = sol.doesValidArrayExist(derived)
    print(f'r  = {r}')
    r1 = sol.doesValidArrayExist_1(derived)
    print(f'r1 = {r1}')
    assert(r == r1)
    print('======================')

