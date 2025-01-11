from typing import List
from collections import defaultdict, deque

class Solution:
    #def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
    #    dq = deque()
    #    hsh1, hsh2 = defaultdict(list), defaultdict(list)
    #    for x, y in adjacentPairs:
    #        hsh1[x] += [y]
    #        hsh2[y] += [x]
    #    print(f'\thsh1, hsh2 = {hsh1}, {hsh2}')
    #    dq.append(adjacentPairs[0][0])
    #    dq.append(adjacentPairs[0][1])
    #    print(f'\tdq = {dq}')
    #    #n = dq[1]
    #    #i = 1
    #    #while n is not None:
    #    #    print(f'\t\tn, dq, hsh1, hsh2 = {n}, {dq}, {hsh1}, {hsh2}')
    #    #    if n in hsh1:
    #    #        for v in hsh1[n]:
    #    #            if dq[i-1] == v:
    #    #                #n = None
    #    #                del hsh1[n]
    #    #            else:
    #    #                dq.append(v)
    #    #                n = v
    #    #                del hsh1[n]
    #    #                i += 1
    #    #    elif n in hsh2:
    #    #        for v in hsh2[n]:
    #    #            if dq[i-1] == v:
    #    #                n = None
    #    #            else:
    #    #                dq.append(v)
    #    #                n = v
    #    #                del hsh2[n]
    #    #                i += 1
    #    #    else:
    #    #        n = None
    #    n = dq[0]
    #    i = 0
    #    tmp = None
    #    while n is not None:
    #        print(f'\t\tn, dq, hsh1, hsh2 = {n}, {dq}, {hsh1}, {hsh2}')
    #        if n in hsh1:
    #            for v in hsh1[n]:
    #                if dq[i+1] != v:
    #                    dq.appendleft(v)
    #                    tmp = v
    #                    i = 0
    #            del hsh1[n]
    #            n = dq[0]
    #        elif n in hsh2:
    #            for v in hsh2[n]:
    #                if dq[i+1] != v:
    #                    dq.appendleft(v)
    #                    tmp = v
    #                    i = 0
    #            del hsh2[n]
    #            n = dq[0]
    #        else:
    #            n = None
    #    return list(dq)
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def dfs(node):
            #print(f'\tnode = {node}')
            if node in hsh1:
                for v in hsh1[node]:
                    if v not in self.visited:
                        self.arr.append(v)
                        self.visited.add(v)
                        dfs(v)
            if node in hsh2:
                for v in hsh2[node]:
                    if v not in self.visited:
                        self.arr.append(v)
                        self.visited.add(v)
                        dfs(v)

        cntr = defaultdict(int)
        root = None
        for x, y in adjacentPairs:
            cntr[x] += 1
            cntr[y] += 1
        for k, v in cntr.items():
            if v == 1:
                root = k
                break
        hsh1, hsh2 = defaultdict(list), defaultdict(list)
        for x, y in adjacentPairs:
            hsh1[x] += [y]
            hsh2[y] += [x]
        #print(f'\thsh1, hsh2 = {hsh1}, {hsh2}')
        self.visited = set()
        self.arr = list()
        self.visited.add(root)
        self.arr.append(root)
        dfs(root)
        return self.arr

# Main section
for adjacentPairs in [
                        [[2,1],[3,4],[3,2]],
                        [[4,-2],[1,4],[-3,1]],
                        [[100000,-100000]],
                        [[9,8],[1,2],[5,6],[7,6],[4,3],[5,4],[7,8],[3,2]],
                     ]:
    print(f'adjacentPairs = {adjacentPairs}')
    sol = Solution()
    r = sol.restoreArray(adjacentPairs)
    print(f'r = {r}')
    print('=================================')


