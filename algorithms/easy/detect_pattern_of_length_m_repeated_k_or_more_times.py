from typing import List

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        def repeatPattern(arr, m):
            pattern = arr[:m]
            cnt = 1
            i = m
            #print(f'\t\tpattern, i = {pattern}, {i}')
            while i + m <= len(arr):
                if arr[i:i+m] == pattern:
                    cnt += 1
                    i += m
                else:
                    break
            return cnt

        curr = 0
        for i in range(0, len(arr)):
            curr = repeatPattern(arr[i:], m)
            #print(f'\tchunk, curr = {arr[i:]}, {curr}')
            if curr >= k:
                return True
        return False

# Main section
for arr, m, k in [
                    ([1,2,4,4,4,4], 1, 3),
                    ([1,2,1,2,1,1,1,3], 2, 2),
                    ([1,2,1,2,1,3], 2, 3),
                    ([1,2,1,2,1,1,1,2,1,2,6,6,4,7,4,7,4,7,7,7], 2, 3),
                    ([1,2,1,2,1,1,1,2,1,2,6,6,9,9,9,9,9,9,7,7], 2, 3),
                 ]:
    print(f'arr, m, k = {arr}, {m}, {k}')
    sol = Solution()
    r = sol.containsPattern(arr, m, k)
    print(f'r = {r}')
    print('===================')

