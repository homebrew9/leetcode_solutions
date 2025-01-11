from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        hsh = dict()
        start, end = None, None
        cnt = 0
        zero_count = 0
        for i, v in enumerate(nums):
            if v == 0:
                zero_count += 1
            if v == 1:
                if start is None:
                    start = i
                    end = i
                    cnt = 1
                else:
                    end = i
                    cnt += 1
            else:
                if start is not None:
                    hsh[(start, end)] = cnt
                    start, end = None, None
        if start is not None:
            hsh[(start, end)] = cnt
        if len(hsh) == 0:
            return 0
        if len(hsh) == 1:
            if zero_count == 0:
                return list(hsh.values())[0] - 1
            else:
                return list(hsh.values())[0]
        keys = sorted(list(hsh.keys()))
        max_val = hsh[keys[0]]
        for i in range(1, len(keys)):
            max_val = max(max_val, hsh[keys[i]])
            if keys[i][0] - keys[i-1][1] == 2:
                max_val = max(max_val, hsh[keys[i]] + hsh[keys[i-1]])
        return max_val

# Main section
for nums in [
               [1,1,0,1],
               [0,1,1,1,0,1,1,0,1],
               [1,1,1],
               [1,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1],
               [1,1,1,1,1,1,1],
               [1,1,1,1,1,1,0],
               [0,0,1,1,1,1,1,0,0,1,1,0,1,0],
               [0,0,0,0,0,0,0],
               [0,0,1,1],
               [1,0,1,1,1,1,1,1,0,1,1,1,1,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.longestSubarray(nums)
    print(f'r = {r}')
    print('===================')


