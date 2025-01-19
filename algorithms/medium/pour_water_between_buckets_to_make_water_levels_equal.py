# ==========================================================
# The idea is same as implement double sqrt(double n) using binary search. Below is a template.
# def sqrt_double(x):
#     left, right = (1, x) if x >= 1 else (x, 1)
#     while right - left >= 1e-10:     # precision is 1e-10
#         mid = left + (right - left) / 2
#         if mid * mid <= x:
#             left = mid
#         else:
#             right = mid
#     return right  
# ==========================================================
from typing import List

class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        def is_distribution_possible(n):
            total_in, total_out = 0, 0
            for bucket in buckets:
                if bucket < n:
                    total_in += n - bucket
                else:
                    total_out += bucket - n
            if total_out * (1 - loss/100) >= total_in:
                return True
            return False
        #left = min(buckets)
        #right = sum(buckets) / len(buckets)
        left = 0
        right = max(buckets)
        delta = 1e-5
        while right - left >= delta:
            mid = (left + right) / 2
            valid = is_distribution_possible(mid)
            #print(left, right, mid, valid)
            if not valid:
                right = mid
            else:
                left = mid
        return right

#class Solution:
#    def equalizeWater(self, buckets: List[int], loss: int) -> float:
#        l, r = min(buckets), sum(buckets) / len(buckets) # initialize lowest and highest possible value
#        left_over = 1-loss/100                           # calculate left over ratio
#        def ok(val):                                     # check if reach to an average of `val` is posible
#            cnt = 0
#            for bucket in buckets:
#                if bucket >= val:
#                    cnt += (bucket - val) * left_over    # count left_over after pouring water
#                else:
#                    cnt -= (val - bucket)                # reduce count for those bucket need more water to reach `val`
#            return cnt >= 0
#        while r - l >= 1e-5:                             # by description, epsilon is 1e-5
#            mid = (l + r) / 2                            # binary search
#            print(l, r, mid, ok(mid))
#            if ok(mid):
#                l = mid 
#            else:    
#                r = mid 
#        return r

# Main section
for buckets, loss in [
                        ([1,2,7], 80),
                        ([2,4,6], 50),
                        ([3,3,3,3], 40),
                     ]:
    print(f'buckets, loss = {buckets}, {loss}')
    sol = Solution()
    r = sol.equalizeWater(buckets, loss)
    print(f'r = {r}')
    print('==================')


