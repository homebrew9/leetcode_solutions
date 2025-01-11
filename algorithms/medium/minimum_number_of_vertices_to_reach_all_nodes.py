from typing import List

class Solution:
    #def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    #    isIncomingEdgeExists = [False for _ in range(n)]
    #    for x, y in edges:
    #        isIncomingEdgeExists[y] = True
    #    requiredNodes = list()
    #    for i, v in enumerate(isIncomingEdgeExists):
    #        if not v:
    #            requiredNodes.append(i)
    #    return requiredNodes
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return set(range(n)) - set(v for _,v in edges)

# Main section
for n, edges in [
                   (6, [[0,1],[0,2],[2,5],[3,4],[4,2]]),
                   (5, [[0,1],[2,1],[3,1],[1,4],[2,4]]),
                ]:
    print(f'n, edges = {n}, {edges}')
    sol = Solution()
    r = sol.findSmallestSetOfVertices(n, edges)
    print(f'r = {r}')
    print('===================')


