from typing import List

class Solution:
    #def maxTurbulenceSize(self, arr: List[int]) -> int:
    #    '''
    #       A = [9, 4,  2, 10,  7,  8, 8,  1,  9]
    #           [   1,  1, -1,  1, -1, 0,  1, -1]
    #    '''
    #    def sign(n):
    #        if n > 0: return 1
    #        if n < 0: return -1
    #        return 0
    #    N = len(arr)
    #    if N == 1:
    #        return 1
    #    i, j = 0, 1
    #    res = 0
    #    prev = None
    #    while j < N:
    #        curr = sign(arr[j] - arr[j-1])
    #        if prev is None:
    #            prev = curr
    #        else:
    #            if curr == 0:
    #                res = max(res, j - i)
    #                i = j
    #                prev = None
    #            elif (prev, curr) == (-1, 1) or (prev, curr) == (1, -1):
    #                prev = curr
    #            else:
    #                res = max(res, j - i)
    #                i = j - 1
    #                prev = curr
    #        j += 1
    #    return res
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        '''
           A = [9, 4,  2, 10,  7,  8, 8,  1,  9]
               [   1,  1, -1,  1, -1, 0,  1, -1]
           A = [4, 8, 12, 16]
               [   1,  1,  1]
           A = [100]
               []
           A = [8, 8, 8, 8, 8]
               [   0, 0, 0, 0]
           A = [6, 5,  4,  3,  2,  1]
               [  -1, -1, -1, -1, -1]
        '''
        def sign(n):
            if n > 0: return 1
            if n < 0: return -1
            return 0
        N = len(arr)
        diff = [sign(arr[i] - arr[i-1]) for i in range(1, N)]
        #print(diff)
        res = float('-inf')
        curr = 0
        for i in range(0, len(diff)):
            #print(i, res, curr)
            if diff[i] == 0:
                res = max(res, curr)
                curr = 0
            elif i == 0:
                curr = 1
                res = 1
            elif diff[i] * diff[i-1] == -1:
                curr += 1
            else:
                res = max(res, curr)
                curr = 1
        return 1 if res == float('-inf') else max(res, curr) + 1

# Main section
for arr, ans in [
                   ([9,4,2,10,7,8,8,1,9], 5),
                   ([4,8,12,16], 2),
                   ([100], 1),
                   ([8,8,8,8,8], 1),
                   ([6,5,4,3,2,1], 2),
                   ([20,14,79,53,68,66,18,99,35,0,67,88,96,78,12,59,5,32,15,86,53,69,72,15,68,20,77,29,17,72,28,11,58,12,59,56,34,35,41,12,47,12,70,88,82,97,66,88,98,14,69,52,20,92,61,25,67,85,22,29,53,63,5,22,64,39,66,32,82,4,82,68,32,67,28,82,15,62,44,22,25,6,96,2,86,3,26,9,2,91,87,56,72,11,99,44,36,85,13,21], 10),
                   ([0,1,1,0,1,0,1,1,0,0], 5),
                   ([0,8,45,88,48,68,28,55,17,24], 8),
                   ([37,199,60,296,257,248,115,31,273,176], 5),
                ]:
    print(f'arr, ans = {arr}, {ans}')
    sol = Solution()
    r = sol.maxTurbulenceSize(arr)
    print(f'r = {r}')
    assert(r == ans)
    print('============================')


