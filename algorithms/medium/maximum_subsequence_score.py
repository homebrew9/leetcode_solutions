from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = []
        for x, y in zip(nums1, nums2):
            nums.append((x, y))
        nums.sort(key=lambda x: -x[1])
        print(f'\tnums = {nums}')

        # Min heap
        h = []
        best = 0
        # total => sum of all values in h
        total = 0
        for x, y in nums:
            print(f'\t\t0) x, y = {x}, {y}')
            heapq.heappush(h, x)
            total += x
            print(f'\t\t1) h, total = {h}, {total}')
            if len(h) > k:
                t = heapq.heappop(h)
                total -= t
                print(f'\t\t\t1.1) t, total = {t}, {total}')
            print(f'\t\t2) h, total = {h}, {total}')
            if len(h) == k:
                best = max(best, total * y)
            print(f'\t\t3) h, total, best = {h}, {total}, {best}')
            print('=====')
        return best

# Main section
for nums1, nums2, k in [
                          ([1,3,3,2], [2,1,3,4], 3),
                          ([4,2,3,1,1], [7,5,10,9,6], 1),
                          ([33,57,75,31,53,61,39,6,62,42,37,55,9,99,18,12,1,35,53,8,65,37,1,23,53,56,11,4,54,59,29,3,62,93,2,84,73,59,100,18,17,65,16,57,24,77,30,30,83,78,15,17,41,53,0,45,76,64,1,41,36,66,30,54,21,69,46,99,70,5,68,4,54,69,6,31,62,57,19,64,79,49,4,45,45,85,74,6,19,49,98,69,16,23,52,60,78,48,48,8], [29,16,27,30,84,88,20,77,66,69,84,15,57,49,18,5,74,72,82,20,68,79,47,8,5,29,9,39,13,9,93,48,6,25,8,59,73,70,17,96,94,81,73,93,80,78,68,72,46,32,42,59,79,57,44,100,80,61,20,5,88,63,98,16,53,47,29,50,66,88,50,52,81,50,61,36,74,41,6,43,44,58,20,68,98,42,51,64,18,98,2,26,0,70,68,35,46,70,83,86], 37),
                       ]:
    print(f'nums1, nums2, k = {nums1}, {nums2}, {k}')
    sol = Solution()
    r = sol.maxScore(nums1, nums2, k)
    print(f'r = {r}')
    print('===============')

