from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Sort + Single traversal
        arr.sort()
        res = list()
        min_diff = 10**20
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < min_diff:
                min_diff = diff
                res = [[arr[i-1], arr[i]]]
            elif diff == min_diff:
                res.append([arr[i-1], arr[i]])
        return res
    def minimumAbsDifference_1(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = min([arr[i] - arr[i-1] for i in range(1, len(arr))])
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == min_diff]

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
    r1 = sol.minimumAbsDifference_1(arr)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('==========================')













