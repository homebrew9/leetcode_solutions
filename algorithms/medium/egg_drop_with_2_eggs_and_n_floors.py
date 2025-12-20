class Solution:
    def twoEggDrop(self, n: int) -> int:
        # ==================
        # At first, it seems a Binary Search should work here, but we can only break 2 eggs at most!!
        # Let's say f=7 and N=100. If BSearch is used, we drop eggs as follows (format: floor(does_it_break?)):
        # 50(Y) -> 25(Y) -> 12(Y) -> 6(N) -> 9(Y) -> 7(N) -> 8(Y) = 5 eggs broke in total!
        # Alternate technique:
        #   (A) Drop 1st egg from floor: 10, 20, 30, ... 100.
        #   (B) If 1st egg breaks on 100th floor, then 91 <= f <= 99.
        #   (C) The 2nd egg can be dropped at most 9 times (91..99) to find out f. Answer = 10 + 9 = 19.
        # Here the interval is fixed (10 floors). So depending on the floor the 1st egg breaks, the
        # total drops could vary from (1+9) to (10+9) i.e. from 10 to 19.
        # If interval is variable, then this process is optimized. We want to ensure that:
        # "No matter what the value of f is, it should take the same number of tries to find it."
        # For that to happen, the drops should be as follows:
        # Floor n, then floor n + (n-1), then floor n + (n-1) + (n-2), and so on.
        # As an example, let N = 10.
        #   (1) Drop 1st egg from floor n = 4, then (4+3=) 7, then (4+3+2=) 9.
        #   (2) If 1st egg breaks at n = 4, we test 3 floors (1,2,3) to find f. Tests = 1+3 = 4
        #   (3) If 1st egg breaks at n = 7, we test 2 floors (5,6) to find f. Tests = 2+2 = 4
        #   (4) If 1st egg breaks at n = 9, we test 1 floor (8) to find f. Tests = 3+1 = 4
        #   (5) If 1st egg doesn't break at n = 9, we test 1 floor (10) to find f. Tests = 3+1 = 4
        # Thus, for a given number of floors N, we find x where:
        # x + (x - 1) + (x - 2) + (x - 3) + ... + 3 + 2 + 1 >= N
        # Or Sigma(x) >= N, or x * (x+1) // 2 >= N. The rest is easy to program.
        # Also check out the TED-Ed video: https://www.youtube.com/watch?v=NGtt7GJ1uiM
        # ==================
        res = 0
        step = 0
        while res < n:
            step += 1
            res += step
        return step

# Main section
for n in [
            2,
            100,
            59,
            907,
            1000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.twoEggDrop(n)
    print(f'r = {r}')
    print('===========================')





















