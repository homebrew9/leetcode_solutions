from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # We will need n operations if all elements are distinct and run from
        # 1 to n. Eg. nums = [1,2,3,4,5]. But if we have other distributions:
        # nums = [9,9,9] => we only need 1 operation
        # nums = [5,9,9] => we need 2 operations
        # nums = [5,7,9] => we need 3 operations
        # Thus, we need len(set(A)) operations for all non-zero elements in A.
        return len(set(nums) - {0})

# Main section
for nums in [
               [1,5,0,3,5],
               [0],
               [61,82,42,78,66,3,54,68,99,26,84,78,70,19,31,5,63,36,89,22,2,32,22,25,89,52,85,76,96,87,45,48,85,47,27,83,30,3,58,10,64,59,56,84,83,5,56,92,13,12,75,16,37,31,68,59,41,30,34,13,80,90,42,13,3,10,18,16,2,10,69,66,93,20,33,81,91,50,86,32,34,12,22,40,24,79,1,100,80,83,90,8,3,56,74,2,55,84,33,88],
               [29,27,4,40,6,73,75,29,67,17,1,24,10,94,75,14,91,8,47,19,84,60,94,21,25,39,4,55,3,28,89,37,31,100,51,27,30,93,70,93,2,3,90,16,34,4,85,41,3,7,52,54,43,71,94,63,59,13,7,39,45,56,23,41,57,23,4,51,98,53,58,89,47,26,75,35,16,26,37,54,58,42,69,46,95,66,25,51,8,71,88,79,51,56,2,99,81,44,70,2],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minimumOperations(nums)
    print(f'r = {r}')
    print('==================')


