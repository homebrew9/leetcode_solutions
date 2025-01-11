#
# =================================================================
# The 1st solution is a naive brute force solution. It fails for an array
# that has the same element repeated 100,000 times.
# The 2nd solution uses prefix sums, but it iterates through the given nums
# array to fill in the res array. That results in TLE for the 100,000 element array.
# The 3rd solution is by Qiqi_impact. It iterates through the dictionary values
# to populate the res array. That's much faster!!
# =================================================================
#
from collections import defaultdict
from typing import List

class Solution:
    #def distance(self, nums: List[int]) -> List[int]:
    #    hsh = defaultdict(list)
    #    for i, n in enumerate(nums):
    #        hsh[n] += [i]
    #    res = list()
    #    for i, n in enumerate(nums):
    #        total = sum([abs(i - x) for x in hsh[n]])
    #        res.append(total)
    #    return res
    #def distance(nums):
    #    hsh = defaultdict(list)
    #    for i, n in enumerate(nums):
    #        hsh[n] += [i]
    #    hsh1 = dict()
    #    for k, v in hsh.items():
    #        arr = hsh[k]
    #        h = dict()
    #        h[arr[0]] = arr[0]
    #        for i in range(1, len(arr)):
    #            key = arr[i]
    #            arr[i] += arr[i-1]
    #            h[key] = arr[i]
    #        hsh1[k] = h
    #    res = list()
    #    for i, v in enumerate(nums):
    #        h = hsh1[v]
    #        allSum, allCount = 0, 0
    #        leftSum, leftCount = 0, 0
    #        for k in sorted(h):
    #            allCount += 1
    #            allSum = h[k]
    #            if k <= i:
    #                leftSum = h[k]
    #                leftCount += 1
    #        rightSum = allSum - leftSum
    #        rightCount = allCount - leftCount
    #        distanceSum = (leftCount*i - leftSum) + (rightSum - rightCount*i)
    #        res.append(distanceSum)
    #    return res
    def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
        #print(d)
        ret = [0] * len(nums)
        for k in d:
            s = sum(d[k])
            x = 0
            for i in range(len(d[k])):
                v = d[k][i]
                x += v
                ret[v] = v*(i+1) - x + (s - x) - v*(len(d[k]) - (i+1))
        return ret

# Main section
for nums in [
               [1,3,1,1,2],
               [0,5,3],
               [1,1,1,2,1,2,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.distance(nums)
    print(f'r = {r}')
    print('=====================')

