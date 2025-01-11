from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def answer(curr, value):
            #print(f'\t\tcurr, value, seen = {curr}, {value}, {self.seen}')
            if curr == self.goal:
                return value
            for adj, adj_value in self.graph[curr].items():
                #print(f'\t\t\tadj, adj_value, seen = {adj}, {adj_value}, {self.seen}')
                if adj not in self.seen:
                    #print(f'\t\t\t\t{adj} not in {self.seen}')
                    self.seen.add(adj)
                    #print(f'\t\t\t\tadj added to seen, new seen: {self.seen}')
                    result = answer(adj, value*adj_value)
                    #print(f'\t\t\t\tresult = {result}')
                    if result != -1:
                        return result
                    self.seen.remove(adj)  # backtrack
                    #print(f'\t\t\t\tbacktrack, seen: {self.seen}')
            return -1
        self.graph = defaultdict(dict)
        self.seen = set()  # all visited expressions
        for (a, b), value in zip(equations, values):
            self.graph[a][b] = value
            self.graph[b][a] = 1/value
        print(f'\tgraph = {self.graph}')
        result = list()
        for orig, self.goal in queries:
            if orig in self.graph:
                result.append(answer(orig, 1))
            else:
                result.append(-1)
            self.seen.clear()
        return result

# Main section
for equations, values, queries in [
           ([['a','b'],['b','c']], [2.0,3.0], [['a','c'],['b','a'],['a','e'],['a','a'],['x','x']]),
           ([['a','b'],['b','c'],['bc','cd']], [1.5,2.5,5.0], [['a','c'],['c','b'],['bc','cd'],['cd','bc']]),
           ([['a','b']], [0.5], [['a','b'],['b','a'],['a','c'],['x','y']]),
           ([['a','b'],['b','c'],['c','d'],['a','x'],['x','y'],['y','z']], [1.0,2.0,3.0,1.5,2.5,3.5], [['a','d'],['a','z']]),
           ([['a','b'],['b','c'],['c','d'],['a','x'],['x','y'],['y','z']], [1.0,2.0,3.0,1.5,2.5,3.5], [['d','a'],['z','a']]),
           ([['a','b'],['b','c'],['c','d'],['a','x'],['x','y'],['y','z']], [1.0,2.0,3.0,1.5,2.5,3.5], [['a','d'],['a','z'],['d','a'],['z','a']]),
           ([['a','e'],['b','e']], [4.0,3.0], [['a','b'],['e','e'],['x','x']]),
           ([['a','b'],['b','c'],['c','d'],['a','e'],['x','e']], [1.0,2.0,3.0,4.0,5.0], [['a','x']]),
           ([['a','b'],['c','d']], [1.0,1.0], [['a','c'],['b','d'],['b','a'],['d','c']]),
        ]:
    print(f'equations, values, queries = {equations}, {values}, {queries}')
    sol = Solution()
    r = sol.calcEquation(equations, values, queries)
    print(f'r = {r}')
    print('===================')


