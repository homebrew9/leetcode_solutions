from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.shops = defaultdict(SortedList)   #movie -> (price, shop)
        self.shop_movie = {}    #(shop, movie) -> price
        self.rented = SortedList()  # (price, shop, movie)
        for s, m, p in entries:
            self.shops[m].add((p, s))
            self.shop_movie[s, m] = p

    def search(self, movie: int) -> List[int]:
        return [y for _,y in self.shops[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie[shop, movie]
        self.shops[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_movie[shop, movie]
        self.shops[movie].add((price, shop))
        self.rented.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        return [[y,z] for _,y,z in self.rented[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()

# Main section
#  ['MovieRentingSystem','search','rent','rent','report','drop','search']
#  [[3,[[0,1,5],[0,2,6],[0,3,7],[1,1,4],[1,2,7],[2,1,5]]],[1],[0,1],[1,2],[],[1,2],[2]]

