from typing import List
from collections import Counter
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # We do Binary Search on a (sorted) time array. The minimum time is 1.
        # What's the maximum time? For that, we look at the ranks. For 10 cars:
        # Rank = 1 => repairs 10 cars in 1 * 100 = 100 mins
        # Rank = 2 => repairs 10 cars in 2 * 100 = 200 mins
        # Rank = 3 => repairs 10 cars in 3 * 100 = 300 mins
        # Rank = 4 => repairs 10 cars in 4 * 100 = 400 mins
        # It's not clear why upper bound is min(cntr)*cars^2 i.e. 100 in above case.
        # If the 4 guys work together, will they finish in < 100 mins???
        cntr = Counter(ranks)
        left, right = 1, min(cntr) * cars * cars
        while left < right:
            mid = (left + right) // 2
            # In time (r * n^2), cars fixed = n. Let's call this time "t".
            # So t = r * n^2 => n^2 = t/r => n = sqrt(t/r)
            # In time t => person 0 fixes sqrt(t/r), or sqrt(t/A[0]) cars
            # In time t => person 1 fixes sqrt(t/r), or sqrt(t/A[1]) cars
            # In time t => person 2 fixes sqrt(t/r), or sqrt(t/A[2]) cars
            # Total cars is just a summation over all of them. The "cntr" is
            # just to speed up the process using the frequency values. (We could've
            # iterated over the array as well.)
            # If total_cars is < given cars, not enough time => increase it
            # If total_cars is >= given cars, it is done, but find the *earliest* time
            # when it was done.
            total_cars = sum([math.isqrt(mid//x)*y for x, y in cntr.items()])
            if total_cars < cars:
                left = mid + 1
            else:
                right = mid
        return left

# Main section
for ranks, cars in [
                      ([4,2,3,1], 10),
                      ([5,1,8], 6),
                      ([8,13,13,46,6,78,98,43,56,83], 97),
                      ([8,13,13,46,6,78,98,43,56,83,37,53,13,10,33,40,77,100,99,32,46,51,76,87,14,46,59,44,76,28,56,80,76,29,93,18,77,83,43,22,56,97,64,49,14,55,24,81,53,90], 500),
                   ]:
    print(f'ranks, cars = {ranks}, {cars}')
    sol = Solution()
    r = sol.repairCars(ranks, cars)
    print(f'r = {r}')
    print('===================')

