#
# Commented solution is Brute Force. O(n*m)
# Other solution uses Binary search, so O(n*log(m))
#
from typing import List
class Solution:
    #def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
    #    cnt = 0
    #    for i in arr1:
    #        canBeAdded = True
    #        for j in arr2:
    #            #print(f'{i}, {j}, {abs(i-j)}, {d}')
    #            if abs(i - j) <= d:
    #                canBeAdded = False
    #                break
    #        if canBeAdded:
    #            cnt += 1
    #        #print('=====')
    #    return cnt

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def isValid(n):
            low, high = 0, len(arr2) - 1
            while low <= high:
                mid = (low + high) // 2
                if abs(n - arr2[mid]) <= d:
                    return False
                elif arr2[mid] < n:
                    low = mid + 1
                else:
                    high = mid - 1
            return True

        arr2.sort()
        cnt = 0
        for n in arr1:
            if isValid(n):
                cnt += 1
        return cnt

# Main section
sol = Solution()
for arr1, arr2, d in [
                        ([4,5,8], [10,9,1,8], 2),
                        ([1,4,2,3], [-4,-3,6,10,20,30], 3),
                        ([2,1,100,3], [-5,-2,10,-3,7], 6),
                     ]:
    print(f'arr1, arr2, d = {arr1}, {arr2}, {d}')
    r = sol.findTheDistanceValue(arr1, arr2, d)
    print(f'r = {r}')
    print('======================')

