#
# Does not work. This is a DP problem!!
#
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        hsh = {chr(i+97):i for i in range(26)}
        N = len(s)
        res = 0
        for i in range(0, N):
            #print(f'\ti, ch = {i}, {s[i]}')
            start = i
            cnt = 1
            for j in range(i+1, N):
                #print(f'\t\tj, ch, start, ch, diff = {j}, {s[j]}, {start}, {s[start]}, {abs(hsh[s[j]] - hsh[s[start]])}')
                if abs(hsh[s[j]] - hsh[s[start]]) <= k:
                    cnt += 1
                    start = j
                    #print(f'\t\t\tinside if => cnt, start = {cnt}, {start}')
            #print(f'\tcnt = {cnt}')
            #print('=====')
            res = max(res, cnt)
        return res

# Main section
for s, k in [
               ('acfgbd', 2),
               ('abcd', 3),
               ('abcdprtuv', 2),
               ('upqggturvz', 3),
               ('lvedjqaeildalclmevit', 3),
               ('uqjepjcxtnsafxuowmtsyqjwpmfbdnvfvvjjgddwwtqxdeaamu', 3),
               ('wpmfbdjgddwwtqxdeaamu', 3),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.longestIdealString(s, k)
    print(f'r = {r}')
    print('===================')


