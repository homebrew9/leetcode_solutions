from typing import List

class Solution:
    def oddString(self, words: List[str]) -> str:
        hsh = {chr(i+97):i for i in range(26)}
        diffs = dict()
        for word in words:
            diff_array = tuple([hsh[word[i]] - hsh[word[i-1]] for i in range(1, len(word))])
            if diff_array in diffs:
                diffs[diff_array] += [word]
            else:
                diffs[diff_array] = [word]
        for k in diffs:
            if len(diffs[k]) == 1:
                return diffs[k][0]

# Main section
for words in [
                ['adc','wzy','abc'],
                ['aaa','bob','ccc','ddd'],
                ['ddd','poo','baa','onn'],
             ]:
    print(f'words = {words}')
    sol = Solution()
    r = sol.oddString(words)
    print(f'r = {r}')
    print('=================')


