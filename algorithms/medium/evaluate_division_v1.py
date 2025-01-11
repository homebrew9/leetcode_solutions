#
# Does not work!
#
from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(from_val, to_val, res):
            print(f'\t\tfrom_val, to_val, res = {from_val}, {to_val}, {res}')
            if from_val == to_val:
                return res
            seen.add(from_val)
            r1, r2 = 1.0, 1.0
            for next_val, v in hsh[from_val]:
                if next_val not in seen:
                    print(f'\t\t\tin 1st for loop...; seen = {seen}')
                    r1 = dfs(next_val, to_val, res*v)
                    print(f'\t\t\t\tr1 = {r1}')
            for next_val, v in hsh1[from_val]:
                if next_val not in seen:
                    print(f'\t\t\tin 2nd for loop...; seen = {seen}')
                    r2 = dfs(next_val, to_val, res*v)
                    print(f'\t\t\t\tr2 = {r2}')
            return r1*r2
        hsh = defaultdict(list)
        hsh1 = defaultdict(list)
        for eq, val in zip(equations, values):
            op1, op2 = eq[0], eq[1]
            hsh[op1] += [(op2, val)]
            hsh1[op2] += [(op1, 1.0/val)]
        print(f'\thsh = {hsh}')
        print(f'\thsh1 = {hsh1}')
        res = list()
        for op1, op2 in queries:
            print(f'\top1, op2 = {op1}, {op2}')
            seen = set()
            if (op1 not in hsh) and (op1 not in hsh1):
                tmp = -1.0
            elif (op2 not in hsh) and (op2 not in hsh1):
                tmp = -1.0
            else:
                tmp = dfs(op1, op2, 1.0)
            res.append(tmp)
            print(f'\ttmp = {tmp}')
            print('=====')
        return res

# Main section
for equations, values, queries in [
           #([['a','b'],['b','c']], [2.0,3.0], [['a','c'],['b','a'],['a','e'],['a','a'],['x','x']]),
           #([['a','b'],['b','c'],['bc','cd']], [1.5,2.5,5.0], [['a','c'],['c','b'],['bc','cd'],['cd','bc']]),
           #([['a','b']], [0.5], [['a','b'],['b','a'],['a','c'],['x','y']]),
           ([['a','b'],['b','c'],['c','d'],['a','x'],['x','y'],['y','z']], [1.0,2.0,3.0,1.5,2.5,3.5], [['a','d'],['a','z']]),
           #([['a','b'],['b','c'],['c','d'],['a','x'],['x','y'],['y','z']], [1.0,2.0,3.0,1.5,2.5,3.5], [['d','a'],['z','a']]),
           #([['a','b'],['b','c'],['c','d'],['a','x'],['x','y'],['y','z']], [1.0,2.0,3.0,1.5,2.5,3.5], [['a','d'],['a','z'],['d','a'],['z','a']]),
           #([['a','e'],['b','e']], [4.0,3.0], [['a','b'],['e','e'],['x','x']]),
           #([['a','b'],['b','c'],['c','d'],['a','e'],['x','e']], [1.0,2.0,3.0,4.0,5.0], [['a','x']]),
           #([['a','b'],['c','d']], [1.0,1.0], [['a','c'],['b','d'],['b','a'],['d','c']]),
        ]:
    print(f'equations, values, queries = {equations}, {values}, {queries}')
    sol = Solution()
    r = sol.calcEquation(equations, values, queries)
    print(f'r = {r}')
    print('===================')



