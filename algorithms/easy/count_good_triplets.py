from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        res = 0
        for i in range(0, N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        res += 1
        return res

# Main section
for arr, a, b, c in [
                       ([3,0,1,1,9,7], 7, 2, 3),
                       ([1,1,2,2,3], 0, 0, 1),
                    ]:
    print(f'arr, a, b, c = {arr}, {a}, {b}, {c}')
    sol = Solution()
    r = sol.countGoodTriplets(arr, a, b, c)
    print(f'r = {r}')
    print('========================')

