from collections import Counter
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        '''
            s = "ccccccbbbbbbaaaaaaa" , rl = 2
            {c: 6, b: 6, a: 7}
            [(c, 6), (b, 6), (a, 7)]
            [(c, 6), (b, 1), (a, 7)]
            [(c, 3), (b, 1), (a, 7)]
            [(c, 1), (b, 1), (a, 5)]
        '''
        cntr = Counter(s)
        arr = sorted([[k, v] for k, v in cntr.items()], reverse=True)
        #print(arr)
        N = len(arr)
        i = 0
        res = ''
        while i < N:
            #print(arr, i, arr[i], res)
            if arr[i][1] == 0:
                i += 1
                continue
            use = min(arr[i][1], repeatLimit)
            res += arr[i][0] * use
            arr[i][1] -= use
            if arr[i][1] > 0:
                # Add a smaller character only if we haven't exhausted
                # the frequency of the current character
                j = i + 1
                while j < N and arr[j][1] == 0:
                    j += 1
                if j >= N:
                    break
                res += arr[j][0]
                arr[j][1] -= 1
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


