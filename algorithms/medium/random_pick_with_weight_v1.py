# ===============================================================================================
# So the basic idea here is that:
# 1) if you have a prefix sum array - which is an increasing array since all ints are > 0, and
# 2) if you use a random number to pick an index from the prefix sum array, then
# 3) the indexes of the larger values have greater probability of being chosen!
#
# Let's say: nums = [100,1,3,2,678]. Then prefix array = [100, 101, 104, 106, 784].
# Now, if I use a random weight and find the nearest index corresponding to that weight (from
# the prefix array), then the index will, most likely, be 4 or 0.
# See the code below.
# Binary Search is simple to implement once the logic is clear.
# ===============================================================================================
import random
from collections import Counter

def random_pick_with_weight(nums):
    N = len(nums)
    total = sum(nums)
    pfx = [None for _ in range(N)]
    for i in range(N):
        pfx[i] = nums[i] if i == 0 else pfx[i-1] + nums[i]
    print(f'pfx  = {pfx}')
    res = list()
    # Note that the logic below is similar to "bisect_left"
    for _ in range(1000):
        target = total * random.random()
        left, right = 0, len(pfx) - 1
        while left <= right:
            mid = (left + right) // 2
            if pfx[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        res.append(left)
    return res

# Main section
for nums in [
               [1,2,3,4,5],
               [9,7,5,3,1],
               [100,1,3,2,678],
            ]:
    print(f'nums = {nums}')
    r = random_pick_with_weight(nums)
    print(f'r    = {r}')
    print(f'Cntr = {Counter(r)}')
    print('================')



