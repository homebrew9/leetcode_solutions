# =================================================
# Programs to practice DFS and BFS
# =================================================
from collections import defaultdict

def graphTraversal(root, leaf, edges):
    def dfs(node, leaf, arr):
        #print(f'\tnode, leaf, arr = {node}, {leaf}, {arr}')
        if node == leaf:
            #print(f'\t\t1) In if node == leaf; node, leaf, arr = {node}, {leaf}, {arr}')
            res.append(arr)
            #print(f'\t\t2) In if node == leaf; node, leaf, arr = {node}, {leaf}, {arr}')
            return
        if node not in hsh:
            return
        for x in hsh[node]:
            dfs(x, leaf, arr+[x])
    hsh = defaultdict(list)
    for x, y in edges:
        hsh[x] += [y]
    res = list()
    dfs(root, leaf, [root])
    return res

# Main section
for root, leaf, edges in [
                            (1, 6, [[1,2],[1,3],[2,4],[2,5],[3,4],[3,5],[4,6],[5,6]]),
                            (1, 5, [[1,2],[1,3],[2,3],[2,4],[4,5]]),
                            (1, 6, [[1,2],[1,3],[2,4],[3,5],[4,6],[5,6],[5,7],[7,6]]),
                            (1, 7, [[1,2],[1,3],[2,4],[3,5],[4,6],[5,6],[5,7],[7,6]]),
                         ]:
    print(f'root, leaf, edges = {root}, {leaf}, {edges}')
    r = graphTraversal(root, leaf, edges)
    print(f'r = {r}')
    print('==================')


