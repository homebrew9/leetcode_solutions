from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        garbage_types = ('M', 'P', 'G')
        # Each value is of format: [total_travel_cost, total_pickup_cost]
        # We iterate from the right to the left and update total_travel_cost only once,
        # and it can be easily identified since travel cost cannot be 0.
        # Finally we return the sum of total travel + pickup cost for each key.
        hsh = dict()
        for garbage_type in garbage_types:
            hsh[garbage_type] = [0, 0]
        for i in range(len(garbage)-1, -1, -1):
            item = garbage[i]
            for garbage_type in garbage_types:
                if garbage_type in item:
                    if hsh[garbage_type][0] == 0:
                        hsh[garbage_type][0] += sum(travel[:i])
                    hsh[garbage_type][1] += item.count(garbage_type)
        return sum(sum(v) for v in hsh.values())

    # The official solution, pasted below, is beautiful too!
    def garbageCollection_1(self, garbage: List[str], travel: List[int]) -> int:
        M, P, G = False, False, False
        ans = len(garbage[0])
        for i in range(len(garbage)-1, 0, -1):
            M |= 'M' in garbage[i]
            P |= 'P' in garbage[i]
            G |= 'G' in garbage[i]
            ans += travel[i-1] * (int(M) + int(P) + int(G)) + len(garbage[i])
        return ans

# Main section
for garbage, travel in [
                          (['G','P','GP','GG'] , [2,4,3]),
                          (['MMM','PGM','GP']  , [3,10]),
                          (['G','G','P']       , [7,11]),
                          (['G','G','PP']      , [7,11]),
                       ]:
    print(f'garbage, travel = {garbage}, {travel}')
    sol = Solution()
    r = sol.garbageCollection(garbage, travel)
    print(f'r  = {r}')
    r1 = sol.garbageCollection_1(garbage, travel)
    print(f'r1 = {r1}')
    print('=================')


