from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def determine_child_count(n):
            # Return the number of children who can get n candies
            return sum([x // n for x in candies])
        left, right = 1, sum(candies)
        while left <= right:
            mid = (left + right) // 2
            child_count = determine_child_count(mid)
            if child_count >= k:
                left = mid + 1
            else:
                right = mid - 1
        return right

# Main section
for candies, k in [
                     ([5,8,6], 3),
                     ([2,5], 11),
                     ([538,326,798,923,657,618,58,376,306,138,563,120,789,319,971,585,211,774,329,920,89,626,998,550,307,462,502,983,476,615,623,328,934,691,362,722,6,896,311,94,777,951,290,546,42,418,98,862,846,494,409,32,545,968,17,211,861,5,442,692,471,979,794,779,490,843,319,959,576,823,427,482,324,193,124,816,574,755,740,452,608,74,184,246,115,258,144,322,28,466,96,776,56,328,195,766,351,560,307,850], 137),
                  ]:
    print(f'candies, k = {candies}, {k}')
    sol = Solution()
    r = sol.maximumCandies(candies, k)
    print(f'r = {r}')
    print('=================')

