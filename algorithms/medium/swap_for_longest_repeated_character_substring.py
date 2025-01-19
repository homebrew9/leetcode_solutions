from collections import Counter, defaultdict

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        def is_swap_possible(hsh):
            if len(hsh) == 2 and min(hsh.values()) == 1:
                key1, key2 = hsh.keys()
                if hsh[key1] == 1 and cntr[key2] - hsh[key2] > 0:
                    return True
                if hsh[key2] == 1 and cntr[key1] - hsh[key1] > 0:
                    return True
            return False
        N = len(text)
        cntr = Counter(text)
        print(cntr)
        i, j = 0, 0
        hsh = defaultdict(int)
        res = 0
        while j < N:
            hsh[text[j]] += 1
            if len(hsh) == 1:
                print(f'\tIn if... i, j, hsh, res = {i}, {j}, {hsh}, {res}')
                res = max(res, j - i + 1)
            elif len(hsh) == 2 and min(hsh.values()) == 1:
                print(f'\tIn elif... i, j, hsh, res = {i}, {j}, {hsh}, {res}')
                key1, key2 = hsh.keys()
                if hsh[key1] == 1 and cntr[key2] - hsh[key2] > 0:
                    res = max(res, j - i + 1)
                elif hsh[key2] == 1 and cntr[key1] - hsh[key1] > 0:
                    res = max(res, j - i + 1)
                else:
                    hsh[text[i]] -= 1
                    if hsh[text[i]] == 0:
                        del hsh[text[i]]
                    i += 1
            else:
                print(f'\tIn else... i, j, hsh, res = {i}, {j}, {hsh}, {res}')
                while i <= j and len(hsh) >= 2 and min(hsh.values()) >= 1:
                    print(f'\t\tIn while... i, j, hsh, res = {i}, {j}, {hsh}, {res}')
                    if is_swap_possible(hsh):
                        res = max(res, j - i + 1)
                        break
                    hsh[text[i]] -= 1
                    if hsh[text[i]] == 0:
                        del hsh[text[i]]
                    i += 1
            j += 1
        return res


# Main section
for text, ans in [
                    #('ababa', 3),
                    #('aaabaaa', 6),
                    #('aaaaa', 5),
                    #('abcdef', 1),
                    #('shzxzvrxwf', 2),
                    #('kxxvohpxbxjpknzmkeymczxidvibltvgfjsonlhpecsptesetdqoxzvszzvljuophjbqtnsvgsxvwxeibdpvkpygxvujdnrncjld', 3),
                    #('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccc' , 50),
                    #('abbbcccbbcabacacabccaabacbacacacbabcaabbcccabbcbbaccabccbcacbaaabbcacbcbcbbcacacbaacacbaaabccacbbaccbcaaaaaabbcaccbcacabaaaacbaccbccabbcbaccacaccbbabacccbcccacbcbaacaccccabbbccccabccbaaacbaccccbaabacbbcbabacbbacbbcabaaaaabbbbabcbacbcccabbaabbbacbcbbbbbcccbbcbbccbbabcbababacccacaaccbaaacbbbacaacacccaccabbaabaaabacaaabcacbbbcacbcaccbbcaccccbcacacbaacccbaacbcabbaaabbbacababbabaacccbbcbacbbabaaacaaaabbbbbcbccbcababbacaaabaacbacbccbcbbacabcaaccaacacaaccbaabcaabcacccabbbcbbcaabbabcbbacbcbbcccbcacacccaccbaaaccbac', 8),
                    #('accbbbaaaabbaccbcbbaaccbcaccbaccc', 5),
                    ('aabaaabaaaba', 7),
                 ]:
    print(f'text = {text}')
    sol = Solution()
    r = sol.maxRepOpt1(text)
    print(f'r = {r}')
    assert(r == ans)
    print('===================')

'''
"ababa"
"aaabaaa"
"aaaaa"
"abcdef"
"shzxzvrxwf"
"kxxvohpxbxjpknzmkeymczxidvibltvgfjsonlhpecsptesetdqoxzvszzvljuophjbqtnsvgsxvwxeibdpvkpygxvujdnrncjld"
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccc"
"abbbcccbbcabacacabccaabacbacacacbabcaabbcccabbcbbaccabccbcacbaaabbcacbcbcbbcacacbaacacbaaabccacbbaccbcaaaaaabbcaccbcacabaaaacbaccbccabbcbaccacaccbbabacccbcccacbcbaacaccccabbbccccabccbaaacbaccccbaabacbbcbabacbbacbbcabaaaaabbbbabcbacbcccabbaabbbacbcbbbbbcccbbcbbccbbabcbababacccacaaccbaaacbbbacaacacccaccabbaabaaabacaaabcacbbbcacbcaccbbcaccccbcacacbaacccbaacbcabbaaabbbacababbabaacccbbcbacbbabaaacaaaabbbbbcbccbcababbacaaabaacbacbccbcbbacabcaaccaacacaaccbaabcaabcacccabbbcbbcaabbabcbbacbcbbcccbcacacccaccbaaaccbac"
"accbbbaaaabbaccbcbbaaccbcaccbaccc"
"aabaaabaaaba"
'''

