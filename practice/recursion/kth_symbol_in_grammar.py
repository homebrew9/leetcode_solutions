# ================================
# n=1, s='0'
# n=2, s='01'
# n=3, s='0110'
# n=4, s='01101001'
# ================================

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def solve(row, col, val):
            if row == 1:
                if val == 0:         # True; it is given that we start with 0
                    return 0         # Our initial guess was correct; return it
                else:
                    return 1         # Else return opposite of initial guess
            if col % 2 == 0:
                if val == 0:
                    return solve(row-1, col//2, 0)
                else:
                    return solve(row-1, col//2, 1)
            else:
                if val == 0:
                    return solve(row-1, col//2, 1)
                else:
                    return solve(row-1, col//2, 0)
        return solve(n, k-1, 0)      # Initial guess is 0
    def kthGrammar_1(self, n: int, k: int) -> int:
        # Shortened a bit from the earlier code
        def solve(row, col, val):
            if row == 1:
                return val # At row=1, if val= 0 then our guess was correct.
            if col % 2 == 0:
                return solve(row-1, col//2, val) # if even bit is 0 then its "originator" is also 0
            else:
                return solve(row-1, col//2, 1 if val == 0 else 0)
        return solve(n, k-1, 0)      # Initial guess is 0

# Main section
for n, k in [
               (1, 1),
               (2, 1),
               (2, 2),
               (4, 4),
               (20, 563701),
               (30, 1234),
               (30, 1073741823),
               (20, 309871),
               (30, 524288),
            ]:
    print(f'n, k = {n}, {k}')
    sol = Solution()
    r = sol.kthGrammar(n, k)
    r1 = sol.kthGrammar_1(n, k)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('=================')


