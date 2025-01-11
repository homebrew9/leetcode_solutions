from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.hsh = dict()
        total = sum(nums)
        self.hsh[0] = total
        for i in range(1, len(nums)):
            total -= nums[i-1]
            self.hsh[i] = total
        self.hsh[len(nums)] = 0

    def sumRange(self, left: int, right: int) -> int:
        return self.hsh[left] - self.hsh[right+1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Main section
for nums, sr1, sr2, sr3 in [
                              [[-2,0,3,-5,2,-1], [0,2],[2,5],[0,5]],
                           ]:
    print(f'nums, sr1, sr2, sr3 = {nums}, {sr1}, {sr2}, {sr3}')
    obj = NumArray(nums)
    param1 = obj.sumRange(sr1[0], sr1[1])
    param2 = obj.sumRange(sr2[0], sr2[1])
    param3 = obj.sumRange(sr3[0], sr3[1])
    print(f'param1, param2, param3 = {param1}, {param2}, {param3}')

