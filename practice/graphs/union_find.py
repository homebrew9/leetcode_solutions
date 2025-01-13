# ==============================================================================
# Given n, there is a graph that contains n nodes from 0 to n-1.
# The connections list has nodes [xi, yi] that are connected.
# The queries list has nodes [xi, yi] whose connectivity needs to be queried.
# Return a list of length = queries length that has True at ith index if
# [xi, yi] are connected or False otherwise.
# ==============================================================================

def connectNodes(n, connections, queries):
    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a
    def isConnected(a, b):
        def find_1(a):
            if parent[a] == a:
                return parent[a]
            return find(parent[a])
        root_a = find_1(a)
        root_b = find_1(b)
        return root_a == root_b
    parent = [i for i in range(n)]
    for a, b in connections:
        union(a, b)
    print(f'\tparent = {parent}')
    res = list()
    for a, b in queries:
        res.append(isConnected(a, b))
    return res

# Main section
for n, connections, queries in [
                                  (6, [[0,1],[0,2],[3,4],[5,4]], [[1,2],[3,5],[1,4],[5,0]]),
                               ]:
    print(f'n, connections, queries = {n}, {connections}, {queries}')
    r = connectNodes(n, connections, queries)
    print(f'r = {r}')
    print('====================')

