from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] - mid - 1 < k:
                low = mid + 1
            else:
                high = mid
        return high + k

# Main section
for arr, k in [
                 ([5,6,7,9], 5),
                 ([2,3,4,7,11], 5),
                 ([1,2,3,4], 2),
                 ([1,2,20,21], 5),
                 ([1,2,3,4], 4),
              ]:
    print(f'arr, k = {arr}, {k}')
    sol = Solution()
    r = sol.findKthPositive(arr, k)
    print(f'r = {r}')
    print('=============================')

