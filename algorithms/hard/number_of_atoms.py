from collections import defaultdict

class Solution:
    #def countOfAtoms(self, formula: str) -> str:
    #    def solve(i, hsh):
    #        print(i, hsh)
    #        if i >= N:
    #            return
    #        h = defaultdict(int)
    #        while i < N and formula[i] != '(' and formula[i] != ')':
    #            key, val = '', ''
    #            if i < N and formula[i].isascii() and formula[i].isupper():
    #                key += formula[i]
    #                i += 1
    #            while i < N and formula[i].isascii() and formula[i].islower():
    #                key += formula[i]
    #                i += 1
    #            while i < N and formula[i].isdigit():
    #                val += formula[i]
    #                i += 1
    #            if val == '':
    #                h[key] += 1
    #            else:
    #                h[key] += int(val)
    #        #print(f'\ti, h = {i}, {h}')
    #        if i < N and formula[i] == '(':
    #            i, hsh = solve(i + 1, hsh)
    #            # Merge hsh with h
    #            for k, v in hsh.items():
    #                h[k] += v
    #        if i < N and formula[i] == ')':
    #            factor = ''
    #            i += 1
    #            while i < N and formula[i].isdigit():
    #                factor += formula[i]
    #                i += 1
    #            if factor != '':
    #                for k in h.keys():
    #                    h[k] = h[k] * int(factor)
    #        #print(f'\t\ti, h = {i}, {h}')
    #        # Merge with the dictionary passed as parameter
    #        #for k, v in h.items():
    #        #    hsh[k] += v
    #        #print(f'\t\t\ti, h, hsh = {i}, {h}, {hsh}')
    #        #print('====')
    #        return (i, h)
    #    N = len(formula)
    #    hsh = defaultdict(int)
    #    _, hsh = solve(0, hsh)
    #    res = ''
    #    for k in sorted(hsh):
    #        res += k
    #        v = hsh[k]
    #        if v > 1:
    #            res += str(v)
    #    return res

    def countOfAtoms(self, formula: str) -> str:
        def merge_hashes(h1, h2):
            # Merges hash h2 into hash h1 and returns h1
            for k, v in h2.items():
                h1[k] += v
            return h1
        def process_formula(i, hsh):
            # Processes formula from index i upto closing brace ")" and
            # the multiplying factor after it, and returns the hash
            h = dict()
            key, val = '', ''
            in_multiply_block = False
            factor = ''
            while i < N and formula[i] != ')':
                if in_multiply_block:
                    if formula[i].isdigit():
                        factor += formula[i]

                elif formula[i].isascii() and formula[i].isupper():
                    if key != '':
                        if val == '':
                            h[key] += 1
                        else:
                            h[key] += int(val)
                        key, val = '', ''
                    key += formula[i]
                elif formula[i].isascii() and formula[i].islower():
                    key += formula[i]
                elif formula[i].isdigit():
                    val += formula[i]
                elif formula[i] == ')':
                    if key != '':
                        if val == '':
                            h[key] += 1
                        else:
                            h[key] += int(val)
                        key, val = '', ''
                    in_multiply_block = True
                    factor = ''
                i += 1

# Main section
for formula in [
                  '((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14',
               ]:
    print(f'formula = {formula}')
    sol = Solution()
    r = sol.countOfAtoms(formula)
    print(f'r = {r}')
    print('==================')

