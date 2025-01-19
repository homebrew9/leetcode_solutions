from typing import List
from collections import defaultdict

class TreeNode:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        def buildTree(node):
            if node.val in hsh:
                node.children = [TreeNode(x) for x in hsh[node.val]]
                for child in node.children:
                    buildTree(child)
        def dfs(node):
            least_common_ancestor = None
            count = 0
            for child in node.children:
                lca, ct = dfs(child)
                count += ct
                if lca:
                    least_common_ancestor = lca
            if count == 2:
                if least_common_ancestor is None:
                    return (node.val, 2)
                else:
                    return (least_common_ancestor, 2)
            if count == 1:
                if node.val in (region1, region2):
                    return (node.val, 2)
                else:
                    return (None, 1)
            if node.val in (region1, region2):
                return (None, 1)
            else:
                return (None, 0)
        def find_root(hsh):
            for k in hsh:
                is_root = True
                for v in hsh.values():
                    if k in v:
                        is_root = False
                        break
                if is_root:
                    return k
        hsh = defaultdict(list)
        self.root = None
        for i, v in enumerate(regions):
            key = v[0]
            val = v[1:]
            hsh[key] = val
        rt = find_root(hsh)
        self.root = TreeNode(rt)
        buildTree(self.root)
        res, ct = dfs(self.root)
        return res

# Main section
for regions, region1, region2 in [
                                    ([['Earth','North America','South America'],['North America','United States','Canada'],['United States','New York','Boston'],['Canada','Ontario','Quebec'],['South America','Brazil']], 'Quebec', 'New York'),
                                    ([['Earth', 'North America', 'South America'],['North America', 'United States', 'Canada'],['United States', 'New York', 'Boston'],['Canada', 'Ontario', 'Quebec'],['South America', 'Brazil']], 'Canada', 'South America'),
                                    ([['Earth','North America','South America'],['North America','United States','Canada'],['United States','New York','Boston'],['Canada','Ontario','Quebec'],['South America','Brazil']], 'United States', 'New York'),
                                    ([['Earth','North America','South America'],['North America','United States','Canada'],['United States','New York','Boston'],['Canada','Ontario','Quebec'],['South America','Brazil']], 'Boston', 'New York'),
                                    ([['Earth','North America','South America'],['North America','United States','Canada'],['United States','New York','Boston'],['Canada','Ontario','Quebec'],['South America','Brazil']], 'Boston', 'Brazil'),
                                    ([['North America','United States','Canada'],['United States','New York','Boston'],['Canada','Ontario','Quebec'],['South America','Brazil'],['Earth','North America','South America']], 'Boston', 'Brazil'),
                                 ]:
    print(f'regions, region1, region2 = {regions}, {region1}, {region2}')
    sol = Solution()
    r = sol.findSmallestRegion(regions,region1,region2)
    print(f'r = {r}')
    print('================')


