from collections import Counter

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        cntr = Counter(nums)
        res = list()
        while cntr:
            key_list = sorted(cntr.keys())
            res.extend(key_list)
            for k in key_list:
                cntr[k] -= 1
                if cntr[k] == 0:
                    del cntr[k]
        return res

# Main section
for nums in [
               [3,1,3,2,1,3],
               [7,7,4,4,4],
               [70,48,41,82,11,12,71,43,65,63,15,76,37,81,40,46,67,60,4,53,71,25,72,65,62,90,97,68,48,12,26,25,60,93,24,5,97,70,9,18,46,79,71,30,85,16,94,67,90,81,6,17,17,13,27,65,58,93,67,61,21,58,40,93,17,73,73,60,72,66,34,12,59,50,7],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.rearrangeArray(nums)
    print(f'r = {r}')
    print('===================================')











