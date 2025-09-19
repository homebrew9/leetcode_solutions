from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food = defaultdict(list)
        self.rating = defaultdict(SortedList)
        N = len(foods)
        for i in range(N):
            f, c, r = foods[i], cuisines[i], ratings[i]
            self.rating[c].add([r, f])
            self.food[f] = [c, r]

    def changeRating(self, food: str, newRating: int) -> None:
        c, r = self.food[food]
        self.rating[c].remove([r, food])
        self.rating[c].add([newRating, food])
        self.food[food] = [c, newRating]

    def highestRated(self, cuisine: str) -> str:
        i = len(self.rating[cuisine]) - 1
        rating, food = self.rating[cuisine][i]
        while i >= 0 and self.rating[cuisine][i][0] == rating:
            food = self.rating[cuisine][i][1]
            i -= 1
        return food

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)


# Main section
# ['FoodRatings','highestRated','highestRated','changeRating','highestRated','changeRating','highestRated']
# [[['kimchi','miso','sushi','moussaka','ramen','bulgogi'],['korean','japanese','japanese','greek','japanese','korean'],[9,12,8,15,14,7]],['korean'],['japanese'],['sushi',16],['japanese'],['ramen',16],['japanese']]
#




















