from typing import List

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        res = list()
        for restaurant in restaurants:
            id, rating, vf, mp, md = restaurant
            if (veganFriendly == 0 or vf == veganFriendly) and mp <= maxPrice and md <= maxDistance:
                res.append(restaurant)
        arr = sorted(res, key=lambda x: (-x[1], -x[0]))
        return [x[0] for x in arr]

# Main section
for restaurants, veganFriendly, maxPrice, maxDistance in [
         ([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 1, 50, 10),
         ([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 0, 50, 1),
         ([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 0, 30, 3),
         ([[33433,15456,1,99741,58916],[61899,85406,1,27520,12303],[63945,3716,1,56724,79619]], 0, 91205, 58378),
    ]:
    print(f'restaurants = {restaurants}')
    print(f'veganFriendly, maxPrice, maxDistance = {veganFriendly}, {maxPrice}, {maxDistance}')
    sol = Solution()
    r = sol.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance)
    print(f'r = {r}')
    print('===================')


