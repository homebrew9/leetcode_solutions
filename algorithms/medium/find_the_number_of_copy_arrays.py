from typing import List

class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        N = len(original)
        diff = [0] + [original[i] - original[i-1] for i in range(1, N)]
        for i in range(N):
            if i > 0:
                u, v = bounds[i]
                umod, vmod = start + diff[i], end + diff[i]
                if v < umod or vmod < u:
                    return 0
                start, end = max(umod, u), min(vmod, v)
            else:
                start, end = bounds[i]
            #print(i, start, end)
        return end - start + 1

# Main section
for original, bounds in [
                           ([1,2,3,4], [[1,2],[2,3],[3,4],[4,5]]),
                           ([1,2,3,4], [[1,10],[2,9],[3,8],[4,7]]),
                           ([1,2,1,2], [[1,1],[2,3],[3,3],[2,3]]),
                           ([1,2,1,5], [[201,209],[206,218],[200,250],[209,300]]),
                        ]:
    print(f'original = {original}')
    print(f'bounds   = {bounds}')
    sol = Solution()
    r = sol.countArrays(original, bounds)
    print(f'r = {r}')
    print('================================')


