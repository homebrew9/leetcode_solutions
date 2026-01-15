from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Counting Sort + Single traversal
        mv = min(arr)
        span = max(arr) - mv
        line = [0] * (span + 1)
        for n in arr:
            line[n - mv] += 1
        prev, curr = None, None
        min_diff = 10**20
        res = list()
        for i, v in enumerate(line):
            if v != 0:
                curr = i + mv
                if prev is not None:
                    diff = curr - prev
                    if diff < min_diff:
                        min_diff = diff
                        res = [[prev, curr]]
                    elif diff == min_diff:
                        res.append([prev, curr])
                prev = curr
        return res

# Main section
for arr in [
              [4,2,1,3],
              [1,3,6,10,15],
              [3,8,-10,23,19,-4,-14,27],
              [1,-1],
              [0,1,3],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.minimumAbsDifference(arr)
    print(f'r = {r}')
    print('==========================')





