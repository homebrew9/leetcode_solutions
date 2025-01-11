from typing import List

class Solution:
    #def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    #    def addPaths(node, lst):
    #        if node == N - 1:
    #            self.arr.append(lst)
    #            return
    #        for i in hsh[node]:
    #            addPaths(i, lst+[i])
    #    N = len(graph)
    #    self.arr = list()
    #    hsh = dict()
    #    for i, v in enumerate(graph):
    #        hsh[i] = v
    #    print(f'\thsh = {hsh}')
    #    addPaths(0, [0])
    #    return self.arr

    # The hsh is unnecessary because graph index is the same a hsh key!
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def addPaths(node, lst):
            if node == N - 1:
                self.arr.append(lst)
                return
            for i in graph[node]:
                addPaths(i, lst+[i])
        N = len(graph)
        self.arr = list()
        addPaths(0, [0])
        return self.arr

# Main section
for graph in [
                [[1,2],[3],[3],[]],
                [[4,3,1],[3,2,4],[3],[4],[]],
                [[1,5],[2],[3],[],[3],[4]],
             ]:
    print(f'graph = {graph}')
    sol = Solution()
    r = sol.allPathsSourceTarget(graph)
    print(f'r = {r}')
    print('====================')

