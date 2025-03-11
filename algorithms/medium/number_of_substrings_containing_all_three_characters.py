from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        a_ind, b_ind, c_ind = 0, 0, 0
        hsh = {'a': [], 'b': [], 'c': []}
        for i, v in enumerate(s):
            hsh[v] += [i]
        if len(hsh['a']) == 0 or len(hsh['b']) == 0 or len(hsh['c']) == 0:
            return 0
        #print(hsh)
        max_ind = float('-inf')
        res = 0
        for i, v in enumerate(s):
            if v == 'a':
                if hsh[v][a_ind] < i:
                    a_ind += 1
                if hsh['b'][b_ind] < hsh[v][a_ind] and b_ind < len(hsh['b']) - 1:
                    b_ind += 1
                if hsh['c'][c_ind] < hsh[v][a_ind] and c_ind < len(hsh['c']) - 1:
                    c_ind += 1
            elif v == 'b':
                if hsh[v][b_ind] < i:
                    b_ind += 1
                if hsh['c'][c_ind] < hsh[v][b_ind] and c_ind < len(hsh['c']) - 1:
                    c_ind += 1
                if hsh['a'][a_ind] < hsh[v][b_ind] and a_ind < len(hsh['a']) - 1:
                    a_ind += 1
            else:
                if hsh[v][c_ind] < i:
                    c_ind += 1
                if hsh['a'][a_ind] < hsh[v][c_ind] and a_ind < len(hsh['a']) - 1:
                    a_ind += 1
                if hsh['b'][b_ind] < hsh[v][c_ind] and b_ind < len(hsh['b']) - 1:
                    b_ind += 1
            # If current character is 'a' and max_inds or 'b' or 'c' are less than that of 'a', then end the loop.
            # Do the same for 'b' and 'c'.
            if v == 'a':
                if hsh['b'][b_ind] < hsh['a'][a_ind] or hsh['c'][c_ind] < hsh['a'][a_ind]:
                    break
            elif v == 'b':
                if hsh['c'][c_ind] < hsh['b'][b_ind] or hsh['a'][a_ind] < hsh['b'][b_ind]:
                    break
            elif v == 'c':
                if hsh['a'][a_ind] < hsh['c'][c_ind] or hsh['b'][b_ind] < hsh['c'][c_ind]:
                    break
            max_ind = max(hsh['a'][a_ind], hsh['b'][b_ind], hsh['c'][c_ind])
            res += N - max_ind
            #print(f'a_ind, b_ind, c_ind = {a_ind}, {b_ind}, {c_ind}')
            #print(f"hsh[a][a_ind], hsh[b][b_ind], hsh[c][c_ind] = {hsh['a'][a_ind]}, {hsh['a'][b_ind]}, {hsh['c'][c_ind]}")
            #print(f'i, v, max_ind, res = {i}, {v}, {max_ind}, {res}')
            #print('=====')
        return res

# Main section
for s in [
            'bbacaab',
            'abcabc',
            'aaacb',
            'abc',
            'abbbaaa',
            'ababcbaacccccbbbabccbcaaccbaacaaccbababccccaaacabcccbbccbbaaabbcbacbcacbcbaccbabaabaacbabcabacbcbacb',
            'bcbcacbabaacbccbbcacbccbbbbcbcacbbaccbbabcabcaacbccacaacaccbbbbbabcbbaccccaaabacbaabbbabbcabccccacccccabcbcccbbccaccbcbaaacaaaaccbcaaacbbccaaabacbbbaacababcabbcbcbbabcababcbccbcccbccaabbcccbbaababccbabbbabaabbbaabccaaacbcccccabaccbabacbbbbaabccccbccaaabacaabaccaaabbbcccaacaaccbbbbbabcbacaaaaccbbacabaacaabbccabacaabbbbbaccbbcbaacabcbaaababbabbabbaabaccaaacaabcbbbbccaacacbabbaabcabbccbcbcbacccccbbacabaccaabccacaaacaccabbabacbcbcbacccbaabcbabacbbbccaccacccaacacabcaacbabccccbccbbbacbabbbbaabbbbccaababbbabaacaabbcababcccbbacbbcbaccccaccbcbabaaccccabababcabbbbacabababccbabbbbbcaaaccbbaccbaababacabbbacbcbbbccccbaaacaabcabbccccabcbacbcbacbacbccbccaacabcabbccacaaabbbbaaaabcbbbabccbbbccaabaabcbaaccbabccababbbbcacababcbaccabcbccccbbcaaaacbbbbbccbacacbcbbabcbcbacabaabcbacacabbaababccccccaabcaccbbccabbabbbcacaccaabacbcaccabcaabaaaccaacaaaaaaaabacacbbccacbbaacabcccacaccaabbbacabccbcccacacaaacabacaccccabbcaacaaccaaabbbacaacacaacacbccbacbbbbccbabbaacbcbbabbacacbcccaccaaacabcbbbaacaaccaccccccccbbccaaba',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.numberOfSubstrings(s)
    print(f'r = {r}')
    print('====================')

