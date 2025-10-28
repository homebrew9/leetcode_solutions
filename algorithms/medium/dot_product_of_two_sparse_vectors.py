from typing import List
from collections import defaultdict

class SparseVector:
    def __init__(self, nums: List[int]):
        self.hsh = defaultdict(int)
        for i, v in enumerate(nums):
            if v > 0:
                self.hsh[i] = v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for k, v in vec.hsh.items():
            if k in self.hsh:
                res += v * self.hsh[k]
        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# Main section
#  ([1,0,0,2,3], [0,3,0,4,0]) => 8
#  ([0,1,0,0,0], [0,0,0,0,2]) => 0
#  ([0,1,0,0,2,0,0], [1,0,0,0,3,0,4]) => 6
#  

































