# ================================================================
# Counting Sort: From LeetCode Explore section.
# Pretty simple implementation for small arrays of positive ints.
# ================================================================

def countingSort(nums):
    # With the use of "startingIndices" array
    N = len(nums)
    K = max(nums)
    counts = [0 for _ in range(K+1)]
    for n in nums:
        counts[n] += 1
    startingIndices = [0 for _ in range(K+1)]
    curr = 0
    for i in range(1, K+1):
        curr += counts[i-1]
        startingIndices[i] = curr
    res = [None for _ in range(N)]
    for n in nums:
        ind = startingIndices[n]
        res[ind] = n
        startingIndices[n] += 1
    return res

def countingSort_1(nums):
    # Without the use of "startingIndices" array
    K = max(nums)
    counts = [0 for _ in range(K+1)]
    for n in nums:
        counts[n] += 1
    res = list()
    for i, v in enumerate(counts):
        while v > 0:
            res.append(i)
            v -= 1
    return res

# Main section
for nums in [
               [7,3,2,5,6,10,9,8,1],
               [7,3,2,9,10,5,0,8,1],
               [5,4,5,5,1,1,3],
            ]:
    print(f'nums = {nums}')
    r1 = countingSort(nums)
    print(f'r1   = {r1}')
    r2 = countingSort_1(nums)
    print(f'r2   = {r2}')
    print('Testing assertion...')
    assert(r1 == r2 == sorted(nums))
    print('===========================')

