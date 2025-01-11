from typing import List

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        st = set()
        print(f'\t{nums}')
        while len(nums) > 0:
            min_value = min(nums)
            max_value = max(nums)
            avg = (min_value + max_value) / 2
            st.add(avg)
            nums.remove(min_value)
            nums.remove(max_value)
            print(f'\t\t{nums}')
        print(f'\tst = {st}')
        return len(st)

# Main section
for nums in [
               [4,1,4,0,3,5],
               [1,100],
               [4,4,4,4],
               [1,1,4,4],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.distinctAverages(nums)
    print(f'r = {r}')
    print('================')

