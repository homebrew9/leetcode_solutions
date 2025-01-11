from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        def sumSubarrays(arr, n):
            # Sliding window
            arr_sum = 0
            iter = 0
            while True:
                if iter + n > len(arr):
                    break
                arr_sum += sum(arr[iter:iter+n])
                iter += 1
            return arr_sum

        total = 0
        odd = 1
        while odd <= len(arr):
            curr = sumSubarrays(arr, odd)
            total += curr
            odd += 2
        return total

# Main section
for arr in [
              [1,4,2,5,3],
              [1,2],
              [10,11,12],
              [1],
              [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
              [74,86,63,45,28,68,44,26,52,27,48,8,64,95,97,77,35,33,22,42,85,76,12,20,31,98,70,2,5,21,79,66,29,1,53,25,89,56,83,94,47,39,55,18,75,69,84,71,50,88,36,73,30,38,23,82,11,4,46,17,59,62,43,54,6,51,19,72,13,16,67,93,3,58,92,24,9,87,40,80,61,90,32,57,65,91,7,49,96,14,99,34,41,60,100,37,78,10,81,15],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.sumOddLengthSubarrays(arr)
    print(f'r = {r}')
    print('=================')

