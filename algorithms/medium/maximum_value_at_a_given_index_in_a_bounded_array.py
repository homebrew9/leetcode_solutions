class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def array_sum(v):
            #print(f'\tv = {v}')
            rspan = n - index - 1
            right_slide = min(v - 1, rspan)
            if right_slide == rspan:
                right_sum = (v * rspan) - (rspan * (rspan + 1) // 2)
            else:
                right_ones = rspan - right_slide
                right_sum = (right_slide * (right_slide + 1) // 2) + right_ones
            lspan = index
            left_slide = min(v - 1, lspan)
            if left_slide == lspan:
                left_sum = (v * lspan) - (lspan * (lspan + 1) // 2)
            else:
                left_ones = lspan - left_slide
                left_sum = (left_slide * (left_slide + 1) // 2) + left_ones
            #print(f'\tleft_sum, v, right_sum = {left_sum}, {v}, {right_sum}')
            return left_sum + v + right_sum
        left, right = 1, 10**9
        while left <= right:
            mid = (left + right) // 2
            val = array_sum(mid)
            #print(left, right, mid, val)
            if val <= maxSum:
                left = mid + 1
            else:
                right = mid - 1
        return right

# Main section
for n, index, maxSum in [
                           (4, 2, 6),
                           (6, 1, 10),
                           (10, 4, 37),
                           (2567, 599, 12347),
                        ]:
    print(f'n, index, maxSum = {n}, {index}, {maxSum}')
    sol = Solution()
    r = sol.maxValue(n, index, maxSum)
    print(f'r = {r}')
    print('=====================')


