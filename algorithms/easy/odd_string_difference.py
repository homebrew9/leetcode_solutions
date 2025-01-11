from typing import List

class Solution:
    def oddString(self, words: List[str]) -> str:
        hsh = {chr(i+97):i for i in range(26)}
        diffs = dict()
        diffs1 = dict()
        for word in words:
            diff_array = [hsh[word[i]] - hsh[word[i-1]] for i in range(1, len(word))]
            #print(word, diff_array)
            if not tuple(diff_array) in diffs:
                diffs[tuple(diff_array)] = 1
                diffs1[tuple(diff_array)] = word
            else:
                diffs[tuple(diff_array)] += 1
                diffs1[tuple(diff_array)] = word
        #print(diffs)
        #print('==========')
        for k in diffs:
            if diffs[k] == 1:
                return diffs1[k]

                
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

