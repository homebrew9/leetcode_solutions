class Solution(object):
    def subarrayBitwiseORs(self, A):
        ans = set()
        cur = {0}
        for x in A:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)

# Main section
for arr in [
              [0],
              [1,1,2],
              [1,2,4],
              [687,565,373,177,985,70,604,38,529,556,835,876,576,476,686,960,670,732,895,174,429,226,902,943,643,873,690,361,662,758],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.subarrayBitwiseORs(arr)
    print(f'r   = {r}')
    print('=================')











