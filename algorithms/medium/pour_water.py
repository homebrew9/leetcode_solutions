from typing import List

def pourWater(heights, volume, k):
    #
    # Testcase: ([1,2,3,4,3,2,1,2,3,4,3,2,1], 2, 5),
    # Expected:  [1,2,3,4,3,3,2,2,3,4,3,2,1]
    # Got     :  [2,3,3,4,3,2,1,2,3,4,3,2,1]
    #
    N = len(heights)
    for _ in range(volume):
        i = k
        while i >= 1 and heights[i-1] <= heights[i]:
            i -= 1
        if i < k:
            while i < k and heights[i] >= heights[i+1]:
                i += 1
            if i != k:
                heights[i] += 1
                continue
        i = k
        while i <= N - 2 and heights[i] >= heights[i+1]:
            i += 1
        if i > k:
            while i > k and heights[i] >= heights[i-1]:
                i -= 1
            if i != k:
                heights[i] += 1
                continue
        heights[i] += 1
    return heights


# Main section
for heights, volume, k, expected in [
         ([2,4,6,4,2], 1, 2, [3,4,6,4,2]),
         ([2,4,6,4,2], 2, 2, [4,4,6,4,2]),
         ([2,4,6,4,2], 3, 2, [4,5,6,4,2]),
         ([2,4,6,4,2], 4, 2, [5,5,6,4,2]),
         ([2,4,6,4,2], 5, 2, [5,6,6,4,2]),
         ([2,4,6,4,2], 6, 2, [6,6,6,4,2]),
         ([2,4,6,4,2], 7, 2, [6,6,6,4,3]),
         ([2,4,6,4,2], 8, 2, [6,6,6,4,4]),
         ([2,4,6,4,2], 9, 2, [6,6,6,5,4]),
         ([2,4,6,4,2], 10, 2, [6,6,6,5,5]),
         ([2,4,6,4,2], 11, 2, [6,6,6,6,5]),
         ([2,4,6,4,2], 12, 2, [6,6,6,6,6]),
         ([2,4,6,4,2], 13, 2, [6,6,7,6,6]),
         ([2,4,6,4,2], 14, 2, [6,7,7,6,6]),
         ([2,4,6,4,2], 15, 2, [7,7,7,6,6]),
         ([2,1,1,2,1,2,2], 4, 3, [2,2,2,3,2,2,2]),
         ([1,2,3,4], 2, 2, [2,3,3,4]),
         ([3,1,3], 5, 1, [4,4,4]),
         ([1,2,3,4,3,2,1,2,3,4,3,2,1], 2, 5, [1,2,3,4,3,3,2,2,3,4,3,2,1]),
    ]:
    print(f'heights, volume, k = {heights}, {volume}, {k}')
    r = pourWater(heights, volume, k)
    print(f'r = {r}')
    assert(r == expected)
    print('=====================')


