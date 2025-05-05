from typing import List
from collections import defaultdict

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        G = defaultdict(list)
        for x, y, w in edges:
            G[x].append((y, w))
            G[y].append((x, w))
        #print(G)
        cumPathLen, valToIdxPos = [], defaultdict(list)

        self.ans = 0
        self.minLen = 1

        def dfs(node, prevStart, parent):
            #print('=====')
            #print('node, prevStart, parent = {}, {}, {}'.format(node, prevStart, parent))
            #print('cumPathLen, valToIdxPos = {}, {}'.format(cumPathLen, valToIdxPos))
            #print('self.ans, self.minLen   = {}, {}'.format(self.ans, self.minLen))
            if len(valToIdxPos[nums[node]]) > 0:
                prevStart = max(prevStart, valToIdxPos[nums[node]][-1])
                #print(f'\tInside len(vtip) > 0; prevStart = {prevStart}')
            if len(cumPathLen) > 0:
                L = cumPathLen[-1] if prevStart == -1 else cumPathLen[-1] - cumPathLen[prevStart]
                #print(f'\tInside len(cpl) > 0; L = {L}')
                if L > self.ans:
                    self.ans = L
                    self.minLen = len(cumPathLen) + 1 - (prevStart + 1)
                    #print(f'\t\tInside L > self.ans; now self.ans, self.minLen = {self.ans}, {self.minLen}')
                elif L == self.ans:
                    self.minLen = min(self.minLen, len(cumPathLen) + 1 - (prevStart + 1))
                    #print(f'\t\tInside L = self.ans; now self.ans, self.minLen = {self.ans}, {self.minLen}')
            for child, length in G[node]:
                if child == parent:
                    continue
                valToIdxPos[nums[node]].append(len(cumPathLen))
                if len(cumPathLen) > 0:
                    cumPathLen.append(cumPathLen[-1] + length)
                else:
                    cumPathLen.append(length)
                dfs(child, prevStart, node)
                valToIdxPos[nums[node]].pop()
                cumPathLen.pop()

        dfs(0, -1, -1)
        return [self.ans, self.minLen]

# Main section
for edges, nums in [
                      ([[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], [2,1,2,1,3,1]),
                      ([[1,0,8]], [2,2]),
                   ]:
    print(f'edges, nums = {edges}, {nums}')
    sol = Solution()
    r = sol.longestSpecialPath(edges, nums)
    print(f'r = {r}')
    print('========================')

