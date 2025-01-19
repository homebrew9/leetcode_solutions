#
# It works, but it is a highly inefficient algorithm!! Use prefix sum method instead!
#

import string
from collections import Counter
from collections import defaultdict
from datetime import datetime

class Solution:
    def beautySum(self, s: str) -> int:
        N = len(s)
        res = 0
        for i in range(0, N):
            for j in range(i+1, N):
                if len(set(s[i:j+1])) > 0:
                    cntr = Counter(s[i:j+1])
                    res += max(cntr.values()) - min(cntr.values())
        return res
    #
    # Bit better, but can be simplified by using a frequency array
    #
    def beautySum1(self, s: str) -> int:
        N = len(s)
        hsh = defaultdict(list)
        for ch in string.ascii_lowercase:
            hsh[ch] = [0] * N
        for i, v in enumerate(s):
            hsh[v][i] += 1
        for ch in string.ascii_lowercase:
            for i in range(1, N):
                hsh[ch][i] += hsh[ch][i-1]
        #print(hsh)
        res = 0
        for i in range(0, N):
            chars = set()
            for j in range(i, N):
                #print(i, j, res)
                chars.add(s[j])
                if len(chars) > 0:
                    max_freq, min_freq = float('-inf'), float('inf')
                    for ch in chars:
                        diff = hsh[ch][j] - hsh[ch][i-1] if i > 0 else hsh[ch][j]
                        max_freq = max(max_freq, diff)
                        min_freq = min(min_freq, diff)
                    res += max_freq - min_freq
        return res
    #
    # Simplest and fastest of the three!
    #
    def beautySum2(self, s: str) -> int:
        N = len(s)
        res = 0
        for i in range(N):
            freq = [0] * 26
            for j in range(i, N):
                freq[ord(s[j]) - 97] += 1
                res += max(freq) - min([x for x in freq if x > 0])
        return res

# Main section
for s in [
            'aabcb',
            'aabcbaa',
            'ysuljwgcryszknfuinjcfssgrzeqnnpnnyekjbyxrgnopkcolnqquqrudimizgvsaqsoeyohqamptzvhynggjumctxqhkejtivcrpeywyggdzyvttgbxsyspvmyzzssiogeqqwqugcvfozxqwymeadoekqjwscnycqsrwbnkwnugqdobdynywgsyzxydykmfnigbkkupkahrburiigxuvkerxmoqtmqxkugaeqdpupsmeqwvbvqnjkzmrvsxqvyamqqgdsbhblhndvwcskbsanuyhznfbpfwsbcajlmjetfxlrinktdglksigrmbcadgmravmzwpunbwhteyscpziliackfjndfngqmgpinmmlkrcpbpsevgdlkeaxrxgdnfvgrdundwlcetbkvnbtemvlbascezkgtogrcqgkrcodnnklmmzkazulpqgafxzxjdbfjexymdocvzldznyphfwrcweisaqxilfcemxmzqjfukaxhkofmp',
            'bbbababbabaaaaaabbbbbbababaaaabbbaababaaabbaaababababbaabbaababbaaaabaaaabbbababaababbaabbbbbbabbbbbababbbaabaabbababaabaabbaabaaaabbbbabbaabbaaaaabbbbabaaaaaabaaababaaabaaaabaabababaababbbbaabaaabaaaabbababbabbbabaabbbbaabbababbabaaaabababababbabaabbaabbabbbbabbbbabbbbabbbbaabaaababaabaaabaaaabaabbabaababbbbaaabaaababaaaaaabbbbbbabbbbbbbaababbbbbaabbbabbaabbabbbabbaaabbababbbbbbbabbabaaaabbaaabababaaaaabbbbbbbbbbbbbaabbbabaaaabaaaaabaaabaababbbbbaabaaababbbbaaaabbaabababbabaabaaaabaaabaabbbbbab',
            'edcceeacaccbaaccdaaceadccacebbebebebdcebceddeaacbcccaaddaecacdcaccbddceaadabdaddcecaeebeedabdeabddebeecabdcddbabdebbccaaeacdebddabaebbdecdadcbcecdedcdbdaecbdebeeebaacdeceddabadbaedeedeedeebdadbbeabbdabaacaddbbccdbcbdbaeebcaccdecddedecbaaeabcbbaecacbecdbdeebccdbadeaabaebcbcdadcceeaeaaeeeeabccebabbcbdbdccdccecccdacdbdbeadbdcdccbeaaaeadbebedcededacbddeedbcdddccadbcddcedcbedbaadbeeadeebedebeacbbcbbdaeedbddaeecadaeccdaeeceecdedaaccdcbaeddcbebeebbedadaeedddaaaebeaeecaacccccdbbaddbaeecbcdabeedbeeadeeab',
            'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
         ]:
    print(f's = {s}')
    sol = Solution()
    start = datetime.now()
    r = sol.beautySum(s)
    print(f'r  = {r} ; {(datetime.now() - start).total_seconds()} sec')
    start = datetime.now()
    r1 = sol.beautySum1(s)
    print(f'r1 = {r1} ; {(datetime.now() - start).total_seconds()} sec')
    start = datetime.now()
    r2 = sol.beautySum2(s)
    print(f'r2 = {r2} ; {(datetime.now() - start).total_seconds()} sec')
    print('=================')

