class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        loc = 0
        for c in s:
            ind = t.find(c, loc)
            if ind == -1:
                return False
            loc = ind + 1
        return True


# Main section
sol = Solution()
for s, t, rslt in [
                     ('abc', 'ahbgdc', True),
                     ('axc', 'ahbgdc', False),
                     ('', 'ahbgdc', True),
                     ('abcd', '', False),
                     ('', '', True),
                     ('abcdef', 'abcdef', True),
                     ('abcdef', 'fedcba', False),
                     ('abcd', 'ab', False),
                     ('ab', 'baab', True),
                     ('rjufvjafbxnbgriwgokdgqdqewn', 'mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq', False),
                  ]:
    print(f's = {s} ; t = {t}')
    r = sol.isSubsequence(s, t)
    print(f'r = {r}')
    assert r == rslt 
    print('======================')


