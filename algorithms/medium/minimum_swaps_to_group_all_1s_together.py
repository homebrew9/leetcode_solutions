from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # Intuition - Group the ones *in any place* in the array. The phrase "in any place"
        # is the giveaway. Use sliding window of size = freq_of_ones to see how many swaps
        # are needed.
        N = len(data)
        x = data.count(1)  # Frequency of 1s in the array
        zero_count = 0
        res = float('inf')
        for i in range(N):
            if data[i] == 0:
                zero_count += 1
            if i - x >= 0 and data[i - x] == 0:
                zero_count -= 1
            if i >= x - 1:
                res = min(res, zero_count)
        return res

# Main section
for data in [
               [1,0,1,0,1],
               [0,0,0,1,0],
               [1,0,1,0,1,0,0,1,1,0,1],
               [0,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,0,0],
            ]:
    print(f'data = {data}')
    sol = Solution()
    r = sol.minSwaps(data)
    print(f'r = {r}')
    print('========================')

