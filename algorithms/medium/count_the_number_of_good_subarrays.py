from typing import List
from collections import defaultdict
import math

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        hsh = defaultdict(int)
        total, cnt = 0, 0
        i = 0
        st = set()
        while i < len(nums):
            n = nums[i]
            print(i, n)
            hsh[n] += 1
            if hsh[n] >= 2:
                if n in st:
                    total = math.comb(hsh[n], 2)
                else:
                    st.add(n)
                    total += math.comb(hsh[n], 2)
                print(f'\ttotal = {total}')
                if total >= k:
                    cnt += 1
                print(f'\ttotal, cnt = {total}, {cnt}')
            i += 1
        print(cnt, hsh)
        j = 0
        while j < len(nums):
            n = nums[j]
            hsh[n] -= 1
            if hsh[n] <= 1:
                if n in st:
                    st.remove(n)
            if len(st) >= k:
                cnt += 1
            elif len(st) == 1:
                if math.comb(hsh[n], 2) >= k:
                    cnt += 1
            j += 1
        #print(cnt, hsh)
        return cnt

# Main section
for nums, k in [
                  #([1,1,1,1,1], 10),
                  #([3,1,4,3,2,2,4], 2),
                  #([1,1,1,1,1,1], 10),
                  ([3,3,2,2,4,4], 2),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.countGood(nums, k)
    print(f'r = {r}')
    print('=============')

