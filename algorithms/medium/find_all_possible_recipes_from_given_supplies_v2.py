from typing import List
from collections import defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        def dfs(node):
            if node in supplies_set:
                return True
            if node in recipes_hsh:
                return recipes_hsh[node]
            if node not in hsh:
                return False
            recipes_hsh[node] = False
            for item in hsh[node]:
                if not dfs(item):
                    return False
            recipes_hsh[node] = True
            return recipes_hsh[node]
        supplies_set = set(supplies)
        recipes_hsh = defaultdict(bool)
        hsh = defaultdict(list)
        for r, i in zip(recipes, ingredients):
            hsh[r] = i
        res = list()
        for r in recipes:
            if dfs(r):
                res.append(r)
        return res

# Main section
for recipes, ingredients, supplies in [
                                         (['bread'], [['yeast','flour']], ['yeast','flour','corn']),
                                         (['bread','sandwich'], [['yeast','flour'],['bread','meat']], ['yeast','flour','meat']),
                                         (['bread','sandwich','burger'], [['yeast','flour'],['bread','meat'],['sandwich','meat','bread']], ['yeast','flour','meat']),
                                         (['ju','fzjnm','x','e','zpmcz','h','q'], [['d'],['hveml','f','cpivl'],['cpivl','zpmcz','h','e','fzjnm','ju'],['cpivl','hveml','zpmcz','ju','h'],['h','fzjnm','e','q','x'],['d','hveml','cpivl','q','zpmcz','ju','e','x'],['f','hveml','cpivl']], ['f','hveml','cpivl','d']),
                                      ]:
    print(f'recipes, ingredients, supplies = {recipes}, {ingredients}, {supplies}')
    sol = Solution()
    r = sol.findAllRecipes(recipes, ingredients, supplies)
    print(f'r = {r}')
    print('===================')

