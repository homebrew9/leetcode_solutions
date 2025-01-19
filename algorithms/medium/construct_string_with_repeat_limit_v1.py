from collections import defaultdict
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        '''
            s = "ccccccbbbbbbaaaaaaa" , rl = 2
            {c: 6, b: 6, a: 7}
            [(c, 6), (b, 6), (a, 7)]
            [(c, 6), (b, 1), (a, 7)]
            [(c, 3), (b, 1), (a, 7)]
            [(c, 1), (b, 1), (a, 5)]
            [(z, 6), (y, 3), (x, 1), (w, 5)] , rl = 1 => zyzyzyzxzwzw
        '''
        hsh = defaultdict(int)
        for ch in s:
            hsh[-ord(ch)] += 1
        h = sorted([(k, v) for k, v in hsh.items()])
        heapq.heapify(h)
        res = ''
        while h:
            num, cnt = heapq.heappop(h)
            use = min(cnt, repeatLimit)
            res += chr(-num) * use
            cnt -= use
            if cnt > 0:
                if not h:
                    break
                n, c = heapq.heappop(h)
                res += chr(-n)
                c -= 1
                if c > 0:
                    heapq.heappush(h, (n, c))
                heapq.heappush(h, (num, cnt))
        return res

# Main section
for s, repeatLimit in [
                         ('ccccccbbbbbbaaaaaaa', 2),
                         ('cczazcc', 3),
                         ('aababab', 2),
                         ('xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt', 1),
                         ('zzzzzzyyyxwwwww', 1),
                      ]:
    print(f's, repeatLimit = {s}, {repeatLimit}')
    sol = Solution()
    r = sol.repeatLimitedString(s, repeatLimit)
    print(f'r = {r}')
    print('=====================')



