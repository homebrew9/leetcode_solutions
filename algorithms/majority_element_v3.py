from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # ==========================================
        # Boyer Moore Voting Algorithm
        # (A) Voting phase - determine the last man standing
        majority = len(nums) // 2
        count = 0
        candidate = None
        for num in nums:
            #print(f'\t>>> Now processing: {num}')
            if candidate is None or count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = None
            #print(f'\t\t>>> candidate, count = {candidate}, {count}')
        # (B) Verification phase - verify that the last man standing is indeed the majority!
        # This verification step is needed because if there is no majority then the last man
        # standing is the last array element.
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
        if count <= majority:
            candidate = None
        return candidate

# Main section
sol = Solution()
for nums in [
                 [3,3,5,7,5,7,3,5,7],
                 [1,2,1,3,1,2,1,1,4,1,4,2,1,3,1,1,3,1,4,2,1,1], # Y,G,Y,R,Y,G,Y,Y,B,Y,B,G,Y,R,Y,Y,R,Y,B,G,Y,Y
                 [3,2,3],
                 [2,2,1,1,1,2,2],
                 [1],
                 [2,2],
                 [1,2,1],
            ]:
    print(f'nums = {nums}')
    r = sol.majorityElement(nums)
    print(f'r    = {r}')
    print('===============================')

