#
# The Josephus problem. It can be solved using circular lists, circular linked lists, recursion
# or with a mathematical formula (which has O(N) TC and O(1) SC).
#
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k == 1:
            return n
        killed = set()
        curr = 0
        while len(killed) < n - 1:
            #print(f'\tIteration start: curr, killed = {curr}, {killed}')
            cnt = 1
            while True:
                curr = (curr + 1) % n
                if curr not in killed:
                    cnt += 1
                    if cnt == k:
                        break
            killed.add(curr)
            while (curr % n) in killed:
                curr = (curr + 1) % n
            #print(f'\tIteration end  : curr, killed = {curr}, {killed}')
            #print('=====')
        #print(f'killed = {killed}')
        alive = list(set(range(n)) - killed)[0]
        return alive + 1

# Main section
for n, k in [
               (5, 1),
               (5, 2),
               (5, 3),
               (5, 4),
               (5, 5),
               (6, 5),
               (1, 1),
               (500, 274),
               (500, 1),
               (500, 97),
            ]:
    print(f'n, k = {n}, {k}')
    sol = Solution()
    r = sol.findTheWinner(n, k)
    print(f'r = {r}')
    print('======================')


