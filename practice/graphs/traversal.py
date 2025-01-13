from collections import defaultdict, deque

def BFSTraversal(root, edges):
    hsh = defaultdict(list)
    for x, y in edges:
        hsh[x] += [y]
    dq = deque()
    visited = set()
    res = list()
    dq.append(root)
    visited.add(root)
    res.append(root)
    while dq:
        N = len(dq)
        for _ in range(N):
            cur = dq[0]
            if cur in hsh:
                for v in hsh[cur]:
                    if v not in visited:
                        dq.append(v)
                        visited.add(v)
                        res.append(v)
            dq.popleft()
    return ' -> '.join([str(x) for x in res])


for root, edges in [
                      (1, [[1,2],[1,3],[2,4],[3,5],[4,6],[5,6],[5,7],[7,6]]),
                      (1, [[1,2],[1,3],[2,4],[2,5],[3,6],[3,7],[4,8],[4,9],[5,10],[6,11],[7,12],[7,13]]),
                   ]:
    print(f'root, edges = {root}, {edges}')
    r = BFSTraversal(root, edges)
    print(f'r = {r}')
    print('==========================')


# =======================================================

def DFSTraversal(root, edges):
    def dfs(node):
        if node not in hsh:
            return
        for v in hsh[node]:
            if v not in visited:
                res.append(v)
                visited.add(v)
                dfs(v)
    hsh = defaultdict(list)
    for x, y in edges:
        hsh[x] += [y]
    res = list()
    visited = set()
    res.append(root)
    visited.add(root)
    dfs(root)
    return ' -> '.join([str(x) for x in res])



for root, edges in [
                      (1, [[1,2],[1,3],[2,4],[3,5],[4,6],[5,6],[5,7],[7,6]]),
                      (1, [[1,2],[1,3],[2,4],[2,5],[3,6],[3,7],[4,8],[4,9],[5,10],[6,11],[7,12],[7,13]]),
                   ]:
    print(f'root, edges = {root}, {edges}')
    r = DFSTraversal(root, edges)
    print(f'r = {r}')
    print('==========================')


