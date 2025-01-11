# =====================================================================================================================================
# Using Union-Find algorithm to solve this problem. Use of a list is inefficient; this should be optimized by using a tree instead.
# This logic does not work for the graph shown below:
#  0    2
#  |    |    4
#  1----3
# Whether we use the first "union" function or the second - either way it returns 3 provinces, but the actual answer is 2.
# After all calls to the first "union" function  => parent = [0,2,2,2,4]
# After all calls to the second "union" function => parent = [2,0,2,0,4]
# That's because UNION(2,0) or UNION(0,2) is never called. But 2 and 0 belong to the same province!
#    # ============================================
#    # vokasi_ovlap solution
#    # ============================================
#    class Solution:
#        def findCircleNum(self, A: List[List[int]]) -> int:
#            def union(a,b):
#                if (root_a := find(a)) == (root_b := find(b)):
#                    return False
#                parent[root_b] = root_a
#                return True
#            def find(e):
#                if parent[e] != e:
#                    parent[e] = find(parent[e])
#                return parent[e]
#            N = len(A)
#            parent = [i for i in range(N)]
#            return N - sum(A[i][j] and union(i, j) for i,j in product(range(N), range(N)))
# =====================================================================================================================================

from typing import List

# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         #  def find(u):
#         #      if parent[u] == u:
#         #          return u
#         #      return find(parent[u])
#         #  #def union(u, v):
#         #  #    print(f'\t\tunion({u}, {v})', end='')
#         #  #    u1 = find(u)
#         #  #    v1 = find(v)
#         #  #    print(f' : u = {u}, v = {v}', end='')
#         #  #    if u1 != v1:
#         #  #        parent[v] = u1
#         #  #    print(f' => {parent}')
#         #  def union(u, v):
#         #      print(f'\t\tunion({u}, {v})', end='')
#         #      u = find(u)
#         #      v = find(v)
#         #      print(f' : u = {u}, v = {v}', end='')
#         #      if u != v:
#         #          parent[v] = u
#         #      print(f' => {parent}')

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Using Union-Find algorithm with a list (less efficient than a tree)
        # This algorithm works.
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
            u1 = find(u)
            v1 = find(v)
            if u1 == v1:
                return False
            parent[v1] = u1
            return True
        N = len(isConnected)
        cnt = 0
        parent = [i for i in range(N)]
        for i, v in enumerate(isConnected):
            for j, w in enumerate(v):
                if i != j and w == 1:
                    ret = union(i, j)
                    if ret:
                        cnt += 1
        return N - cnt

# Main section
for isConnected in [
                      [[1,1,0],[1,1,0],[0,0,1]],
                      [[1,0,0],[0,1,0],[0,0,1]],
                      [[1,1,0,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,1,1,1,0],[0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,1,0,1,0],[0,0,0,0,0,0,0,0,0,1]],
                      [[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1]],
                      [[1,1,1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0],[1,0,0,1,1,0,0,0,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,1,1,1,0],[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,0,0,1]],
                      [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,0,0,0,1]],
                      [[1,1,0,0,0],[1,1,0,1,0],[0,0,1,1,0],[0,1,1,1,0],[0,0,0,0,1]],
                      [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]],
                      [[1,1,1,0,1,1,1,0,0,0],[1,1,0,0,0,0,0,1,0,0],[1,0,1,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0,1,0],[1,0,0,1,1,0,0,0,0,0],[1,0,0,0,0,1,0,0,0,0],[1,0,0,0,0,0,1,0,1,0],[0,1,0,0,0,0,0,1,0,1],[0,0,0,1,0,0,1,0,1,1],[0,0,0,0,0,0,0,1,1,1]],
                   ]:
    print(f'isConnected = {isConnected}')
    sol = Solution()
    r = sol.findCircleNum(isConnected)
    print(f'r = {r}')
    print('==================')


