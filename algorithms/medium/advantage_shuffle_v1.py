# ==========================================================================================
# Approach 1: Greedy
# 
# Intuition
# If the smallest card a in A beats the smallest card b in B, we should pair them.
# Otherwise, a is useless for our score, as it can't beat any cards.
# Why should we pair a and b if a > b?
# Because every card in A is larger than b, any card we place in front of b will score
# a point. We might as well use the weakest card to pair with b as it makes the rest
# of the cards in A strictly larger, and thus have more potential to score points.
# 
# Algorithm
# We can use the above intuition to create a greedy approach.
# The current smallest card to beat in B will always be b = sortedB[j].
# For each card a in sortedA, we will either have a beat that
# card b (put a into assigned[b]), or throw a out (put a into remaining).
# 
# Afterwards, we can use our annotations assigned and remaining to reconstruct the answer.
# ==========================================================================================
from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        snums1 = sorted(nums1)
        snums2 = sorted(nums2)
        assigned = { x: [] for x in nums2 }
        remaining = list()
        j = 0
        for n in snums1:
            if n > snums2[j]:
                assigned[snums2[j]] += [n]
                j += 1
            else:
                remaining.append(n)
        res = list()
        for n in nums2:
            if len(assigned[n]) > 0:
                tmp = assigned[n].pop()
            else:
                tmp = remaining.pop()
            res.append(tmp)
        return res

# Main section
for nums1, nums2 in [
                       ([1,2,3,4], [1,2,3,4]),
                       ([1,9,9,9,1,6,9],[9,4,3,2,1,10,5]),
                       ([31,55,90,71,36,77,41,31,2,14],[82,95,26,79,41,3,85,96,23,91]),
                       ([9,1,2,4,5],[6,2,9,1,4]),
                    ]:
    print(f'nums1, nums2 = {nums1}, {nums2}')
    sol = Solution()
    r = sol.advantageCount(nums1, nums2)
    print(f'r = {r}')
    print('====================')


