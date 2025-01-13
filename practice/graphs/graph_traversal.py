from collections import defaultdict, deque

def graphTraversalDFS(root, edges):
    def dfs(node, arr):
        if node not in hsh:
            res.append(arr)
            return
        for x in hsh[node]:
            dfs(x, arr+[x])
    hsh = defaultdict(list)
    for x, y in edges:
        hsh[x] += [y]
    res = list()
    arr = list()
    arr.append(root)
    dfs(root, arr)
    return res


def graphTraversalBFS(root, edges):
    def bfs(node, arr):
        hsh = defaultdict(list)
        for x, y in edges:
            hsh[x] += [y]
        dq = deque()
        seen = set()
        dq.append(root)
        seen.add(root)
        res = list()
        res.append(root)
        while dq:
            N = len(dq)
            for _ in range(N):
                cur = dq[0]
                for x in hsh[cur]:
                    if x not in seen:
                        seen.add(x)
                        dq.append(x)
                        res.append(x)
                dq.popleft()
        return res
    return bfs(root, [])


for root, edges in [
                      (1, [[1,2],[1,3],[2,4],[3,5],[4,6],[5,6],[5,7],[7,6]]),
                      (1, [[1,2],[1,3],[2,4],[2,5],[3,4],[3,5],[4,6],[5,6]]),
                   ]:
    print(f'root, edges = {root}, {edges}')
    r = graphTraversalDFS(root, edges)
    print(f'DFSL: r = {r}')
    r = graphTraversalBFS(root, edges)
    print(f'BFS: r = {r}')
    print('===================')


