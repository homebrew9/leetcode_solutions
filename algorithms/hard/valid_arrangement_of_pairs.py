#
# Hierholzer's algorithm for Eulerian path. This is the iterative solution.
# Check editorial for the recursive solution as well.
#
from typing import List
from collections import defaultdict

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adjacencyMatrix = defaultdict(list)
        inDegree, outDegree = defaultdict(int), defaultdict(int)

        # Build the adjacency list and track in-degrees and out-degrees
        for pair in pairs:
            start, end = pair[0], pair[1]
            adjacencyMatrix[start].append(end)
            outDegree[start] += 1
            inDegree[end] += 1

        result = []

        # Find the start node (outDegree == inDegree + 1)
        startNode = -1
        for node in outDegree:
            if outDegree[node] == inDegree[node] + 1:
                startNode = node
                break

        # If no such node exists, start from the first pair's first element
        if startNode == -1:
            startNode = pairs[0][0]

        nodeStack = [startNode]

        # Iterative DFS using stack
        while nodeStack:
            node = nodeStack[-1]
            if adjacencyMatrix[node]:
                # Visit the next node
                nextNode = adjacencyMatrix[node].pop(0)
                nodeStack.append(nextNode)
            else:
                # No more neighbors to visit, add node to result
                result.append(node)
                nodeStack.pop()

        # Reverse the result since we collected nodes in reverse order
        result.reverse()

        # Construct the result pairs
        pairedResult = []
        for i in range(1, len(result)):
            pairedResult.append([result[i - 1], result[i]])

        return pairedResult

# Main section
for pairs in [
                [[5,1],[4,5],[11,9],[9,4]],
                [[1,3],[3,2],[2,1]],
                [[1,2],[1,3],[2,1]],
             ]:
    print(f'pairs = {pairs}')
    sol = Solution()
    r = sol.validArrangement(pairs)
    print(f'r = {r}')
    print('==================')


