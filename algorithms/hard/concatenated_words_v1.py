from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)
        print(f'\td = {d}')

        def dfs(word):
            self.indent += '\t'
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                print(f'{self.indent}i, word, prefix, suffix = {i}, {word}, {prefix}, {suffix}')
                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True
                if suffix in d and dfs(prefix):
                    return True
            return False

        res = []
        for word in words:
            self.indent = '\t'
            print(f'\tword = {word}')
            if dfs(word):
                res.append(word)
        return res

# Main section
for words in [
                ['cat','cats','catsdogcats','dog','dogcatsdog','hippopotamuses','rat','ratcatdogcat'],
                ['cat','dog','catdog'],
                ['ab','cd', 'abcd'],
                ['abcd', 'ab','cd'],
                ['aa','bb','cc','bbaacc'],
             ]:
    print(f'words = {words}')
    sol = Solution()
    r = sol.findAllConcatenatedWordsInADict(words)
    print(f'r = {r}')
    print('================')


