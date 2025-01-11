from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cntr = Counter(words)
        hsh = dict()
        for key, val in cntr.items():
            if val not in hsh:
                hsh[val] = [key]
            else:
                hsh[val] += [key]
        print(f'\thsh = {hsh}')
        arr = list()
        for key in reversed(sorted(hsh)):
            for i in sorted(hsh[key]):
                arr.append(i)
                k -= 1
                if k == 0:
                    return arr
        return arr

# Main section
for words, k in [
                   (['i','love','leetcode','i','love','coding'], 2),
                   (['i','love','leetcode','i','love','coding'], 3),
                   (['i','love','leetcode','i','love','coding'], 4),
                   (['i','love','leetcode','i','love','coding'], 1),
                   (['the','day','is','sunny','the','the','the','sunny','is','is'], 4),
                   (['p','p','p','p','a','a','a','a','y','y','y','y','m','m','m','b','b','b','d','e'], 2),
                   (['p','p','p','p','a','a','a','a','y','y','y','y','m','m','m','b','b','b','d','e'], 3),
                   (['p','p','p','p','a','a','a','a','y','y','y','y','m','m','m','b','b','b','d','e'], 4),
                   (['p','p','p','p','a','a','a','a','y','y','y','y','m','m','m','b','b','b','d','e'], 5),
                   (['p','p','p','p','a','a','a','a','y','y','y','y','m','m','m','b','b','b','d','e'], 6),
                   (['p','p','p','p','a','a','a','a','y','y','y','y','m','m','m','b','b','b','d','e'], 7),
                ]:
    print(f'words, k = {words}, {k}')
    sol = Solution()
    r = sol.topKFrequent(words, k)
    print(f'r = {r}')
    print('=============================')

