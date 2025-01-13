#
# Find the shortest path between two given nodes of a graph.
#
from collections import deque, defaultdict

def bfs(edges, root, target):
    hsh = defaultdict(list)
    for x, y in edges:
        hsh[x] += [y]
    dq = deque()
    vis = set()
    dq.append(root)
    vis.add(root)
    step = 0
    while dq:
        #print(f'\tdq, step = {dq}, {step}')
        size = len(dq)
        for _ in range(size):
            cur = dq[0]
            if cur == target:
                return step
            for v in hsh[cur]:
                if not v in vis:
                    dq.append(v)
                    vis.add(v)
            dq.popleft()
        step += 1
    return -1  # target not in graph!

# Main section
for edges, root, target in [
                              ([[0,1],[0,2],[0,3],[1,4],[2,5],[3,5],[3,7],[4,6],[5,6],[6,7]], 0, 0),
                              ([[0,1],[0,2],[0,3],[1,4],[2,5],[3,5],[3,7],[4,6],[5,6],[6,7]], 0, 1),
                              ([[0,1],[0,2],[0,3],[1,4],[2,5],[3,5],[3,7],[4,6],[5,6],[6,7]], 0, 2),
                              ([[0,1],[0,2],[0,3],[1,4],[2,5],[3,5],[3,7],[4,6],[5,6],[6,7]], 0, 3),
                              ([[0,1],[0,2],[0,3],[1,4],[2,5],[3,5],[3,7],[4,6],[5,6],[6,7]], 0, 4),
                              ([[0,1],[0,2],[0,3],[1,4],[2,5],[3,5],[3,7],[4,6],[5,6],[6,7]], 0, 5),
                              ([[0,1],[0,2],[0,3],[1,4],[2,5],[3,5],[3,7],[4,6],[5,6],[6,7]], 0, 6),
                              ([[0,1],[0,2],[0,3],[1,4],[2,5],[3,5],[3,7],[4,6],[5,6],[6,7]], 0, 7),
                              ([[0,1],[0,2],[0,3],[1,4],[2,5],[3,5],[3,7],[4,6],[5,6],[6,7]], 0, 9),
                           ]:
    print(f'edges, root, target = {edges}, {root}, {target}')
    r = bfs(edges, root, target)
    print(f'r = {r}')
    print('==================')


