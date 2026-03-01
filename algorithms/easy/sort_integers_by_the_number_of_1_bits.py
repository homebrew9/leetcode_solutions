from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def get_bits(n):
            cnt = 0
            while n > 0:
                cnt += n & 1
                n >>= 1
            return cnt
        return sorted(arr, key=lambda x: (get_bits(x), x))

# Main section
for arr in [
              [0,1,2,3,4,5,6,7,8],
              [1024,512,256,128,64,32,16,8,4,2,1],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.sortByBits(arr)
    print(f'r = {r}')
    print('=================================================')
 


