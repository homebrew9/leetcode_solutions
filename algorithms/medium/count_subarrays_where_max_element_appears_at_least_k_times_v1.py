from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''
        This can be solved using two-pointer approach, where we find the smallest subarray containing
        max_val k times. We next find the distances (d1 and d2) of the left and right indexes from the
        ends and multiply them (d1*d2). For the next occurrence of such a pair, we only consider the
        subarray that starts from the element after the previous occurrence of left index. E.g.
                0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5  6  7
        nums = [1, 2, 1, 2, 3, 2, 1, 3, 1, 1, 1, 2, 3, 2, 3, 1, 2, 1] ; k = 2. Here, N = 18
                            i        j              m     n
                            4        7             12    14
        For (i, j) array is nums[0:] => (left_distance) * (right_distance) = ( 4 +  1) * (18 -  7) = 5 * 11 = 55
        For (j, m) array is nums[5:] => (left_distance) * (right_distance) = ( 7 -  4) * (18 - 12) = 3 *  6 = 18
        For (m, n) array is nums[8:] => (left_distance) * (right_distance) = (12 -  7) * (18 - 14) = 5 *  4 = 20
        Answer = 55 + 18 + 20 = 93
        So now if we have only the list of indexes where the max value occurs then we can perform the
        above calculation by iterating that list.
        '''
        N = len(nums)
        max_val = max(nums)
        indexes = [i for i, v in enumerate(nums) if v == max_val]
        M = len(indexes)
        if M < k:
            return 0
        res = 0
        prev_ind = -1
        for i in range(0, M - k + 1):
            curr_ind = indexes[i]
            next_ind = indexes[i + k - 1]
            res += (curr_ind - prev_ind) * (N - next_ind)
            prev_ind = curr_ind
        return res

# Main section
for nums, k in [
                  ([1,3,2,3,3], 2),
                  ([1,4,2,1], 3),
                  ([1,7,2,3,7,4,5,7,3], 2),
                  ([3,3,3,3], 1),
                  ([3,3,3,3], 2),
                  ([3,3,3,3], 3),
                  ([3,3,3,3], 4),
                  ([3,3,3,3], 5),
                  ([61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82], 2),
                  ([19,32,59,25,61,15,11,77,95,16,47,15,97,91,90,14,87,73,30,11,11,89,57,95,16,84,14,6,18,47,8,6,91,74,16,25,87,38,91,89,90,65,28,81,23,27,80,53,66,72,44,24,1,14,73,95,78,21,50,60,56,2,20,15,65,13,96,68,63,54,27,19,11,56,18,81,7,99,28,15,41,87,91,1,56,61,66,96,70,22,73,100,95,80,10,42,6,30,7,58,71,88,60,28,4,96,78,52,27,79,45,28,94,49,95,89,81,99,73,95,14,33,39,85,19,72,2,96,11,49,39,38,42,74,50,41,90,97,29,42,92,95,70,37,61,53,98,4,84,39,63,26,2,50,94,81,74,75,99,19,50,69,50,93,23,1,3,78,52,58,50,95,85,36,2,25,76,24,15,53,43,7,35,33,96,29,99,51,57,1,51,85,58,27,36,93,48,41,78,43,34,36,30,13,38,46,52,27,8,22,67,45,86,50,38,52,57,95,55,6,85,68,69,58,90,73,65,30,79,39,22,100,23,78,30,37,65,100,42,91,48,35,70,71,38,61,4,1,80,44,99,100,46,10,21,1,23,53,83,13,17,77,78,77,91,34,48,9,53,42,61,78,19,89,72,37,3,54,34,12,17,17,26,8,97,36,3,83,17,56,36,16,88,30,38,24,65,32,84,18], 3),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.countSubarrays(nums, k)
    print(f'r = {r}')
    print('==================')

