from typing import List
from collections import defaultdict

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set('aeiou')
        word_set = set(wordlist)
        hsh = defaultdict(list)
        hsh1 = defaultdict(list)
        for word in wordlist:
            hsh[word.lower()] += [word]
            key = ''.join(['_' if ch in vowels else ch for ch in word.lower()])
            hsh1[key] += [word]
        res = list()
        for query in queries:
            if query in word_set:
                res.append(query)
            elif query.lower() in hsh:
                # Capitalization check
                res.append(hsh[query.lower()][0])
            else:
                # Vowel error check
                q = ''.join(['_' if ch in vowels else ch for ch in query.lower()])
                if q in hsh1:
                    res.append(hsh1[q][0])
                else:
                    res.append('')
        return res

# Main section
for wordlist, queries in [
                            (['KiTe','kite','hare','Hare'], ['kite','Kite','KiTe','Hare','HARE','Hear','hear','keti','keet','keto']),
                            (['yellow'], ['YellOw']),
                            (['HmYKBE', 'YsryIg'], ['ObTSutI', 'GjUNeAZ', 'bPPCykc', 'uIXDKcG']),
                            (['ERYxyrf'], ['eKR', 'LWV', 'eYZ']),
                            (['f', 'L', 'F', 'b', 'c', 'y', 'j'], ['W', 'm', 'h', 'J', 'L', 'B', 'X']),
                            (['nJCKqT', 'JGpdbh', 'KvinUF', 'xpItif', 'QVqXBr', 'ekhaBk'], ['qHN', 'dQq', 'zGG', 'krx', 'ngR', 'ali', 'lWZ']),
                            (['vU', 'uV', 'Ta', 'lw', 'AO'], ['LZYiyG', 'zJAJdm', 'ebFbzK', 'sNpJhf', 'ZCTssC', 'LieLmF', 'lTYweb']),
                            (['zeo','Zuo'], ['zuo']),
                         ]:
    print(f'wordlist = {wordlist}')
    print(f'queries  = {queries }')
    sol = Solution()
    r = sol.spellchecker(wordlist, queries)
    print(f'r = {r}')
    print('===================')



































