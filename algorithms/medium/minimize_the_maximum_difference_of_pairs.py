from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        
        # Find the number of valid pairs by greedy approach
        def countValidPairs(threshold):
            index, count = 0, 0
            while index < n - 1:
                # If a valid pair is found, skip both numbers.
                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            return count
        
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2

            # If there are enough pairs, look for a smaller threshold.
            # Otherwise, look for a larger threshold.
            if countValidPairs(mid) >= p:
                right = mid
            else:
                left = mid + 1
        return left

# Main section
for nums, p in [
                  ([10,1,2,7,1,3], 2),
                  ([4,2,1,2], 1),
                  ([29,32,31,0,32,67,67,45,12,65,69,84,97,34,68,68,4,97,20,37,85,24,37,67,40,59,18,44,1,18], 11),
                  ([86,77,60,48,18,87,6,35,6,38,61,64,70,96,11,3,13,69,100,81,35,91,66,38,88,71,52,56,31,39,38,78,82,45,98,79,21,58,20,43,7,99,11,68,54,38,83,9,36,19], 23),
               ]:
    print(f'nums, p = {nums}, {p}')
    sol = Solution()
    r = sol.minimizeMax(nums, p)
    print(f'r  = {r}')
    print('===================')





