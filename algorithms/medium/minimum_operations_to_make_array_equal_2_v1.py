from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            if nums1 != nums2:
                return -1
            return 0
        totalDelta = 0
        delta = 0
        moves = 0
        for a, b in zip(nums1, nums2):
            #print('%10s %10s %10s %10s'%(a, b, (a-b), (a - b)//k))
            delta = a - b
            if delta % k != 0:
                return -1
            totalDelta += delta
            moves += abs((a - b)//k)
            #print('%10s %10s %10s %10s %10s %10s %10s'%(a, b, (a-b), (a - b)//k, delta, totalDelta, moves))

        if totalDelta != 0:
            return -1
        return moves // 2

# Main section
for nums1, nums2, k in [
                          ([15,31,20,3,28,19], [36,31,14,0,34,1], 3),
                          ([4,3,1,4], [1,3,7,1], 3),
                          ([3,8,5,2], [2,4,1,6], 1),
                          ([10,20,30], [6,28,26], 2),
                          ([3,8,5,2], [2,8,7,1], 1),
                          ([4,3,1,4], [2,3,6,1], 10),
                       ]:
    print(f'nums1, nums2, k = {nums1}, {nums2}, {k}')
    sol = Solution()
    r = sol.minOperations(nums1, nums2, k)
    print(f'r = {r}')
    print('===============')


