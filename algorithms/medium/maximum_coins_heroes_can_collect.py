#
# Three similar solutions using prefix sums and binary search.
#
from typing import List
import bisect

class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        '''
            mc = [(1,2), (1,3), (2,5), (3,6), (5,4)]
        '''
        monsters_coins = sorted([(m, c) for m, c in zip(monsters, coins)])
        mlist = [m for m, c in monsters_coins]
        clist = [c for m, c in monsters_coins]
        pfx = [0 for _ in range(len(clist))]
        for i in range(len(clist)):
            pfx[i] = (0 if i == 0 else pfx[i-1]) + clist[i]
        res = list()
        for i, v in enumerate(heroes):
            left, right = 0, len(mlist) - 1
            while left <= right:
                mid = (left + right) // 2
                if mlist[mid] <= v:
                    left = mid + 1
                else:
                    right = mid - 1
            ind = bisect.bisect_right(mlist, v)
            if ind == 0:
                res += [0]
            else:
                res += [pfx[ind-1]]
        return res
    def maximumCoins_1(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        '''
            mc = [(1,2), (1,3), (2,5), (3,6), (5,4)]
        '''
        monsters_coins = sorted([(m, c) for m, c in zip(monsters, coins)])
        mlist = [m for m, c in monsters_coins]
        clist = [c for m, c in monsters_coins]
        pfx = [0 for _ in range(len(clist))]
        for i in range(len(clist)):
            pfx[i] = (0 if i == 0 else pfx[i-1]) + clist[i]
        res = list()
        for i, v in enumerate(heroes):
            left, right = 0, len(mlist) - 1
            while left <= right:
                mid = (left + right) // 2
                if mlist[mid] <= v:
                    left = mid + 1
                else:
                    right = mid - 1
            ind = left
            #ind = bisect.bisect_right(mlist, v)
            if left == 0:
                res += [0]
            else:
                res += [pfx[left-1]]
        return res
    def maximumCoins_2(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        '''
            mc = [(1,2), (1,3), (2,5), (3,6), (5,4)]
        '''
        monsters_coins = sorted([(m, c) for m, c in zip(monsters, coins)])
        mlist = [m for m, c in monsters_coins]
        clist = [c for m, c in monsters_coins]
        pfx = [0 for _ in range(len(clist))]
        for i in range(len(clist)):
            pfx[i] = (0 if i == 0 else pfx[i-1]) + clist[i]
        res = list()
        for i, v in enumerate(heroes):
            left, right = 0, len(mlist) - 1
            while left <= right:
                mid = (left + right) // 2
                if mlist[mid] <= v:
                    left = mid + 1
                else:
                    right = mid - 1
            ind = left
            #ind = bisect.bisect_right(mlist, v)
            if right < 0:
                res += [0]
            else:
                res += [pfx[right]]
        return res

# Main section
for heroes, monsters, coins in [
                                  ([1,4,2], [1,1,5,2,3], [2,3,4,5,6]),
                                  ([5], [2,3,1,2], [10,6,5,2]),
                                  ([4,4], [5,7,8], [1,1,1]),
                                  ([34,64,78,93,69,23,59,66,4,61,11,5,74,9,77,99,25,44,35,49,7,50,91,37,89,21,84,15,14,43,98,46,74,18,65,66,71], [10,66,48,74,63,45,11,1,61,87,14,52,41,93,78,30,23,8,91,60,30,10,99,36,58,68,4,44,32,30,68,13,90,93,11,3,97,80,30,1,9,70,88,7,92,27,3,46,24,91,29,88,28,94,30,32,74,34,55,36,65,23,35,45,77,30,52,15,11,96,32,88,14,18,72,3,53,82,22,71,61,18,79,15,53,56,37,48,35,77,82,6,28,39,14,64,51,48,26,73], [56,42,93,25,45,39,26,65,1,55,56,68,75,81,33,32,31,37,39,21,28,12,1,19,83,37,85,8,66,26,33,32,24,78,27,79,77,6,62,48,3,35,58,52,69,15,34,32,58,93,38,99,6,66,63,74,63,100,33,72,37,98,43,46,20,34,19,54,97,34,45,75,48,1,24,71,29,47,56,7,82,8,77,34,36,5,41,53,56,70,71,76,60,29,30,85,55,40,82,70]),
                               ]:
    print(f'heroes, monsters, coins = {heroes}, {monsters}, {coins}')
    sol = Solution()
    r = sol.maximumCoins(heroes, monsters, coins)
    print(f'r  = {r}')
    r1 = sol.maximumCoins_1(heroes, monsters, coins)
    print(f'r1 = {r1}')
    r2 = sol.maximumCoins_2(heroes, monsters, coins)
    print(f'r2 = {r2}')
    print('=================')


