#
# Does not work for last test case.
#

#from collections import deque, defaultdict
#
#class Solution:
#    def findRotateSteps(self, ring: str, key: str) -> int:
#        def bfs(node, pos):
#            dq = deque()
#            seen = set()
#            dq.append(node)
#            seen.add(node)
#            steps = 0
#            while dq:
#                size = len(dq)
#                for _ in range(size):
#                    curr = dq.popleft()
#                    if ring[curr] == key[pos]:
#                        return (curr, steps + 1)
#                    for next_idx in hsh[curr]:
#                        if next_idx not in seen:
#                            seen.add(next_idx)
#                            dq.append(next_idx)
#                steps += 1
#        N = len(ring)
#        hsh = defaultdict(list)
#        for i in range(N):
#            hsh[i] += [(i + 1)%N]
#            hsh[(i + 1)%N] += [i]
#        M = len(key)
#        res = 0
#        pos = 0
#        for i in range(M):
#            (pos, steps) = bfs(pos, i)
#            res += steps
#        return res

from collections import deque
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        def get_neighbor(i):
            left = i - 1 if i > 0 else n - 1
            right = i + 1 if i < n - 1 else 0
            return left, right
        dq = deque([(0, 0)])
        visited = set(dq)
        steps = 0
        while dq:
            for _ in range(len(dq)):
                pos, kidx = dq.popleft()
                if kidx == len(key):
                    return steps
                if ring[pos] == key[kidx]:
                    if (pos, kidx+1) not in visited:
                        dq.append((pos, kidx+1))
                        visited.add((pos, kidx+1))
                else:
                    l, r = get_neighbor(pos)
                    if (l, kidx) not in visited:
                        dq.append((l, kidx))
                        visited.add((l, kidx))
                    if (r, kidx) not in visited:
                        dq.append((r, kidx))
                        visited.add((r, kidx))
            steps += 1
        return -1


# Main section
for ring, key in [
                    #('godding', 'diddddddddddddddidididididididididididididididididididididid'),
                    #('obpyuzhxsm', 'ympszbzzmohzuszxymbyypmxpuzbhmumszuyzuxuooboyhbhoy'),
                    #('obpyuzhxsm', 'mbxuouxhsyzobxsuooxuyoboyxmzmzzuxuuhuhxyyxyhhzspzbuhoshbsuuphmhuhxyhzybbmypzbbpbsuxosbbmpspbsupuhxyp'),
                    #('yrtaebcnwzsfhsffaumrfktjuwvmgjiqnvninehedsedypgcijpcckyssxfqdpddjaacnvcxwatptentrssvdzvahzbmmkmbajzx', 'ezyrcezczzaecwttazeeebwbnrznteyzyartybzctacwcccytyayarreanawabryweatwwrrwtrbtzrzeeabrewywryrwwwtyctz'),
                    ('daudr', 'urdda'),
                 ]:
    print(f'ring, key = {ring}, {key}')
    sol = Solution()
    r = sol.findRotateSteps(ring, key)
    print(f'r = {r}')
    print('==================')

