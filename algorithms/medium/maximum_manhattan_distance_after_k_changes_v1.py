class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # A bit trickier, but requires only one iteration. The idea is to get the overall
        # displacement so far in each iteration. Let's say the string so far is: "EEEEWWEE"
        # We would want to change the W's to E's here i.e. one with lower frequency "mnlr".
        # But we can only change k occurrences of W. So we derive "take" = min(k, mnlr).
        # When we do change the W's, then "cur" would increase by twice of "take":
        #    - first "take" characters to reverse the W's
        #    - next "take" characters to add the desired delta
        # The "if" branches for processing left/right and up/down can be swapped; their
        # effects are independent of each other.
        # Best to try out with pen and paper to see its working.
        up, down, left, right = 0, 0, 0, 0
        ans = 0
        for ch in s:
            if ch == 'N':
                up += 1
            elif ch == 'S':
                down += 1
            elif ch == 'E':
                right += 1
            elif ch == 'W':
                left += 1
            cur = abs(up-down) + abs(left-right)
            k_copy = k
            if left > 0 and right > 0:
                mnlr = min(left, right)
                take = min(k_copy, mnlr)
                cur += 2 * take
                k_copy -= take
            if up > 0 and down > 0:
                mnud = min(up, down)
                take = min(k_copy, mnud)
                cur += 2 * take
                k_copy -= take
            ans = max(ans, cur)
        return ans

# Main section
for s, k in [
               ('NWSE', 1),
               ('NSWWEW', 3),
               ('NSES', 1),
               ('EWWE', 1),
               ('WEEW', 3),
               ('WEWE', 1),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.maxDistance(s, k)
    print(f'r = {r}')
    print('=======================')

