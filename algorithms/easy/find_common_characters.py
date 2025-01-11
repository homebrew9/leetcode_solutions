from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cntr = None
        for word in words:
            if cntr == None:
                cntr = Counter(word)
            else:
                cntr = cntr & Counter(word)
        return list(cntr.elements())

# Main section
for words in [
                ['bella', 'label', 'roller'],
                ['cool', 'cook', 'lock'],
             ]:
    print(f'words = {words}')
    sol = Solution()
    r = sol.commonChars(words)
    print(f'r = {r}')
    print('=============================')

