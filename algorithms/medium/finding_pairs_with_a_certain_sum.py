from typing import List
from collections import Counter

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.cntr1 = Counter(nums1)
        self.nums2 = nums2
        self.cntr2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]
        new = old + val
        self.nums2[index] = new
        self.cntr2[old] -= 1
        if self.cntr2[old] == 0:
            del self.cntr2[old]
        self.cntr2[new] += 1

    def count(self, tot: int) -> int:
        res = 0
        for k in self.cntr1:
            if tot - k in self.cntr2:
                res += self.cntr1[k] * self.cntr2[tot - k]
        return res

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

# Main section
#["FindSumPairs","count","add","count","count","add","add","count"]
#[[[1,1,2,2,2,3],[1,4,5,2,5,4]],[7],[3,2],[8],[4],[0,1],[1,1],[7]]
















