class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        f, pre = [0] * n, [0] * n
        f[0] = 1
        # since we start dynamic programming from i=minJump, we need to precompute the prefix sums for the part [0, minJump)
        for i in range(minJump):
            pre[i] = 1
        for i in range(minJump, n):
            left, right = i - maxJump, i - minJump
            if s[i] == "0":
                total = pre[right] - (0 if left <= 0 else pre[left - 1])
                f[i] = int(total != 0)
            pre[i] = pre[i - 1] + f[i]

        return bool(f[n - 1])

# Main section
for s, minJump, maxJump in [
                              ('011010', 2, 3),
                              ('01101110', 2, 3),
                           ]:
    print(f's, minJump, maxJump = {s}, {minJump}, {maxJump}')
    sol = Solution()
    r = sol.canReach(s, minJump, maxJump)
    print(f'r = {r}')
    print('==================================')












