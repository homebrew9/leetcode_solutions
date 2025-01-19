# ==========================================================
# Proofs for why greedy is sufficient for this problem.
# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/discuss/585632/JavaC%2B%2BPython-Easy-Prove
# https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem
# https://codeforces.com/blog/entry/67171
# ==========================================================

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # Greedy algorithm. Make sure to understand the proof by @lee215 as to
        # why greedy is sufficient!
        fibo = [1, 1]
        while (v := fibo[-1] + fibo[-2]) <= k:
            fibo.append(v)
        #print(fibo)
        res = 0
        for n in reversed(fibo):
            while k - n >= 0:
                k -= n
                res += 1
        return res

# Main section
for k in [
            7,
            10,
            19,
            1000000000,
            227327651,
         ]:
    print(f'k = {k}')
    sol = Solution()
    r = sol.findMinFibonacciNumbers(k)
    print(f'r = {r}')
    print('=================')


