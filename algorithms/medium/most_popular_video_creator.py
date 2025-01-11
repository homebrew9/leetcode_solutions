from typing import List

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        hsh1 = dict()
        hsh2 = dict()
        for c, i, v in zip(creators, ids, views):
            if c in hsh1:
                views_sum = hsh1[c][0] + v
                views_max = max(hsh1[c][1], v)
                hsh1[c] = [views_sum, views_max] 
            else:
                hsh1[c] = [v, v]
            #if c in hsh2:
            #    if v > hsh2[c][1]:
            #        if i < hsh2[c][0]:
            #            hsh2[c] = [i, v]
            #else:
            #    hsh2[c] = [i, v]
        print(f'\thsh1 = {hsh1}')
        highest_views = 0
        for k, v in hsh1.items():
            if v[0] > highest_views:
                highest_views = v[0]
        print(f'\thighest_views = {highest_views}')

        for c, i, v in zip(creators, ids, views):
            if c in hsh2:
                if v == hsh1[c][1]:
                    if i < hsh2[c]:
                        hsh2[c] = i
            else:
                if v == hsh1[c][1]:
                    hsh2[c] = i

        print(f'\thsh2 = {hsh2}')
        arr = list()
        for k, v in hsh1.items():
            if v[0] == highest_views:
                arr.append([k, hsh2[k]])
        return arr

# Main section
for creators, ids, views in [
                               (['alice','bob','alice','chris'], ['one','two','three','four'], [5,10,5,4]),
                               (['alice','alice','alice'], ['a','b','c'], [1,2,2]),
                               (['a','b','a','c','b','c'], ['p','r','q','q','r','r'], [2,2,2,2,2,2]),
                            ]:
    print(f'creators, ids, views = {creators}, {ids}, {views}')
    sol = Solution()
    r = sol.mostPopularCreator(creators, ids, views)
    print(f'r = {r}')
    print('================')

