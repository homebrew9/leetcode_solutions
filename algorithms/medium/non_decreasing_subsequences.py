from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        sequence = list()

        def backtrack(index):
            #print(f'index, sequence, result = {index}, {sequence}, {result}')
            #print('%2d, %-15s, %s'%(index,sequence,result))
            self.calls += 1
            if index == len(nums):
                if len(sequence) >= 2:
                    result.add(tuple(sequence))
                return
            if not sequence or sequence[-1] <= nums[index]:
                sequence.append(nums[index])
                backtrack(index + 1)
                sequence.pop()
            backtrack(index + 1)

        self.calls = 0
        backtrack(0)
        #print(self.calls)
        return result

# Main section
for nums in [
               [4,6,7,7],
               [4,4,3,2,1],
               #[1,2,3,1,5],
               #[1,2,3],
               #[1,2],
               #[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findSubsequences(nums)
    print(f'r = {r}')
    print('===============')

